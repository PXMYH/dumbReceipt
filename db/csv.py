import csv


def write_csv(items):
    with open("receipt_records.csv", "a", newline="") as csvfile:
        receipt_writer = csv.writer(csvfile, delimiter=" ")
        receipt_writer.writerows(items)
