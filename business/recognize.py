from adapters.mindee_adapter import mindee_adapter
from adapters.veryfi_adapter import veryfi_adapter
from db.csv import write_csv
from db.models import Product, db
from datetime import datetime

import csv

import configs.app_config as app_config


def remove_duplicates(items):
    # TODO: super not efficient and super bad code, but quick and get the job done for now
    with open("receipt_records.csv", newline="") as csvfile:
        receipts_reader = csv.reader(csvfile, delimiter=" ")
        for item in items:
            for row in receipts_reader:
                if item == row:
                    # remove the record
                    items.remove(item)

    return items


def convert_datetime(datetime_string):
    datetime_format = "%Y-%m-%d %H:%M:%S"
    converted_datetime = datetime.strptime(datetime_string, datetime_format)
    return converted_datetime


def recognize():
    print("recognizing ...")

    if app_config.OCR_ENGINE_SUPPLIER == "VERYFI":  # TODO: move "VERYFI" as enum
        items = veryfi_adapter()
        print(f"recognized items = {items}")

        # verify items doesn't contain duplicates
        items = remove_duplicates(items)

        # write to csv file
        write_csv(items)

        # write to database
        for item in items:
            product = Product(
                name=item[-2],
                quantity=item[-1],
                price=item[3],
                vendor=item[7],
                created_at=convert_datetime(item[0]),
            )
            # Add the product to the database, not efficient, should explore batch write
            db.session.add(product)
            db.session.commit()

        return items
    else:
        mindee_adapter()
