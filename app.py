import logging
import os
from pathlib import Path
from typing import List, Tuple
from flask import Flask, flash, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from db.connect import connect_database
from controllers import Receipt
import configs.app_config as app_config

UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER", "./uploads/receipts")
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

connect_database(app)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def remove_previous_receipt_files(receipt_dir: str) -> None:
    """Remove existing receipt files except for .gitkeep"""
    for f in os.listdir(receipt_dir):
        if not f.endswith(".gitkeep"):
            file_path = Path(receipt_dir) / f
            with file_path.open("w") as f:
                f.unlink()

@app.route("/")
def upload_page():
    return render_template("upload.html")

@app.route("/", methods=["GET", "POST"])
def uploader() -> str:
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)

        # remove existing receipts
        receipt_dir = Path(app_config.RECEIPT_FILE_DIR).resolve()
        logger.debug(f"removing previous receipt files in {receipt_dir}")
        remove_previous_receipt_files(receipt_dir)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = receipt_dir / filename
            file.save(file_path)
            # TODO: replace with saving the file to a remote storage
            # return redirect(url_for("upload_page", name=filename))
            return redirect(url_for("process", name=filename))

        return f"file {secure_filename(file.filename)} uploaded successfully"

@app.route("/process")
def process() -> str:
    # initialize receipt engine
    receipt_engine = Receipt.Receipt()

    try:
        # start the receipt import engine
        ingestion_result = receipt_engine.ingest()

        # start the receipt processing engine
        receipt_engine.run()

        return f"<div>Success! {ingestion_result} </div>"

    finally:
        # close the app if necessary
        receipt_engine.shutdown()

if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s")
    app.run(debug=True)
