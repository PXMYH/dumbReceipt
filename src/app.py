from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from db.connect import connect_database
from controllers import Receipt

app = Flask(__name__)

connect_database(app)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return f'file {secure_filename(f.filename)} uploaded successfully'

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

if __name__ == '__main__':
    app.run(debug=True)
