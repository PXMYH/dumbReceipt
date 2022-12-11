from adapters.midee_adapter import mindee_adapter
from adapters.veryfi_adapter import veryfi_adapter
from db.csv import write_csv
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


def recognize():
    print("recognizing ...")

    if app_config.OCR_ENGINE_SUPPLIER == "VERYFI":  # TODO: move "VERYFI" as enum
        items = veryfi_adapter()
        print(f"recognized items = {items}")

        # verify items doesn't contain duplicates
        items = remove_duplicates(items)

        # write to csv file
        write_csv(items)
        return items
    else:
        mindee_adapter()
