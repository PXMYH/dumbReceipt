import csv


def write_csv(items):
    with open("receipt_records.csv", "a") as csvfile:
        receipt_writer = csv.writer(csvfile, delimiter=" ")
        for item in items:
            receipt_writer.writerow(item)
