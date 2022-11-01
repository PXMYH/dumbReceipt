import os
from flask import Flask, flash, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from db.connect import connect_database
from controllers import Receipt

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

connect_database(app)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload")
def upload_file():
    return render_template("upload.html")


@app.route("/uploader", methods=["GET", "POST"])
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

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for("upload_file", name=filename))

        return f"file {secure_filename(file.filename)} uploaded successfully"


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


if __name__ == "__main__":
    app.run(debug=True)
