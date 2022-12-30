import csv


def write_csv(items):
    with open("receipt_records.csv", "a") as csvfile:
        receipt_writer = csv.writer(csvfile, delimiter=" ")
        for item in items:
            print(f"preparing to write item {item}")
            receipt_writer.writerow(item)
