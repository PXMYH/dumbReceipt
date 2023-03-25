import os
from flask import Flask, flash, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from db.connect import connect_database
from controllers import Receipt
import configs.app_config as app_config

UPLOAD_FOLDER = "./uploads/receipts"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}

app = Flask(__name__)

connect_database(app)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def upload_page():
    return render_template("upload.html")


@app.route("/", methods=["GET", "POST"])
def uploader():
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
        current_dir = os.path.dirname(__file__)
        print(f"current directory: {current_dir}")
        receipt_dir = current_dir + "/" + app_config.RECEIPT_FILE_DIR
        print("removing previous receipt files...")
        [
            os.remove(receipt_dir + "/" + f)
            for f in os.listdir(receipt_dir)
            if not f.endswith(".gitkeep")
        ]

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(receipt_dir, filename))
            # TODO: replace with saving the file to a remote storage
            # return redirect(url_for("upload_page", name=filename))
            return redirect(url_for("process", name=filename))

        return f"file {secure_filename(file.filename)} uploaded successfully"


@app.route("/process")
def process():
    # initialize receipt engine
    receiptEngine = Receipt.Receipt()

    try:
        # start the receipt import engine
        ingestion_result = receiptEngine.ingest()

        # start the receipt processing engine
        receiptEngine.run()

        return f"<div>Success! {ingestion_result} </div>"

    finally:
        # close the app if necessary
        receiptEngine.shutdown()


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
