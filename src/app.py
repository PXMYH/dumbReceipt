from flask import Flask
from controllers import Receipt

app = Flask(__name__)


@app.route("/")
def main():
    # initialize receipt engine
    receiptEngine = Receipt.Receipt()

    try:
        # start the receipt import engine
        receiptEngine.ingest()

        # start the receipt processing engine
        receiptEngine.run()
        return "<div>Success!</div>"

    finally:
        # close the app if necessary
        receiptEngine.shutdown()
