from business.load import load
from business.recognize import recognize
from db.models import Product, db


class Receipt:
    def __init__(self) -> None:
        print("initializing Receipt Engine ...")

    def ingest(self):
        """
        read in receipt and ocr
        for now supports ingest receipt one by one, support for batch import is planned in the future
        """
        print("running ingesting engine ...")

        load()
        result = recognize()
        return result

    def run(self):
        # categorize_receipt()
        print("running receipt engine ...")

    def shutdown(self):
        print("closing receipt engine ...")

    def get_all_receipts(self):
        products = Product.query.all()
        return products
