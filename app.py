import os
from flask import (
    Flask,
    flash,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
)
from werkzeug.utils import secure_filename
from db.connect import connect_database
from controllers import Receipt
import configs.app_config as app_config

UPLOAD_FOLDER = "./uploads/receipts"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}

app = Flask(__name__)

connect_database(app)


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
        receipt_dir = os.path.join(
            os.path.dirname(__file__), app_config.RECEIPT_FILE_DIR
        )
        [
            os.remove(os.path.join(receipt_dir, f))
            for f in os.listdir(receipt_dir)
            if not f.endswith(".gitkeep")
        ]

        if (
            file
            and secure_filename(file.filename)
            and "." in file.filename
            and file.filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
        ):
            filename = secure_filename(file.filename)
            file.save(os.path.join(receipt_dir, filename))
            return redirect(url_for("process", name=filename))

        flash("Invalid file type. Only txt, pdf, png, jpg, jpeg, and gif are allowed.")
        return redirect(request.url)

    return render_template("upload.html")


@app.route("/uploads/receipts/<name>")
def serve_uploaded_file(name):
    receipt_dir = os.path.join(os.path.dirname(__file__), app_config.RECEIPT_FILE_DIR)
    return send_from_directory(receipt_dir, name)


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


@app.route("/receipts")
def display_receipts():
    # initialize receipt engine
    receiptEngine = Receipt.Receipt()

    receipts = receiptEngine.get_all_receipts()
    return render_template("receipts.html", receipts=receipts)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
