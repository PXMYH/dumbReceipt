from adapters.mindee_adapter import MindeeAdapter
from adapters.veryfi_adapter import VeryfiAdapter
from db.csv import write_csv
from db.models import Product, db
from datetime import datetime

import csv

import configs.app_config as app_config

# remove duplicate record in the receipt_records.csv file when new record is added
def remove_duplicates(items):
    with open("receipt_records.csv", "r", newline="") as csvfile:
        receipts_reader = csv.reader(csvfile, delimiter=" ")

        # read existing records into a set for faster lookup
        existing_records = set(tuple(row) for row in receipts_reader)

    # filter out items that already exist in the CSV file
    new_records = [item for item in items if tuple(item) not in existing_records]

    return new_records


# convert datetime to a specific format
def convert_datetime(datetime_string):
    datetime_format = "%Y-%m-%d %H:%M:%S"
    converted_datetime = datetime.strptime(datetime_string, datetime_format)
    return converted_datetime


def recognize():
    print("recognizing ...")

    if app_config.OCR_ENGINE_SUPPLIER == "MINDEE":  # TODO: move "VERYFI" as enum
        adapter = MindeeAdapter()
        adapter.process_documents()
        return

    if app_config.OCR_ENGINE_SUPPLIER == "VERYFI":
        adapter = VeryfiAdapter()
        items = adapter.process_documents()
        print(f"recognized items = {items}")

        # verify items doesn't contain duplicates
        items = remove_duplicates(items)

        # write to csv file
        write_csv(items)

        # write to database
        products = []
        for item in items:
            product = Product(
                name=item[-2],
                quantity=item[-1],
                price=item[3],
                vendor=item[7],
                created_at=convert_datetime(item[0]),
            )
            products.append(product)

        db.session.add_all(products)
        db.session.commit()

        return items

    raise NotImplementedError("The specified adapter is not implemented yet.")
