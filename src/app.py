from flask import Flask, render_template, request
from controllers import Receipt
from db.connect import connect_database
from werkzeug.utils import secure_filename

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

# db = SQLAlchemy()
app = Flask(__name__)

# db_name = 'receipt.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db.init_app(app)

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

    # connect to database
    # try:
    #     db.session.query(text('1')).from_statement(text('SELECT 1')).all()
    #     return '<h1>It works.</h1>'
    # except Exception as e:
    #     # e holds description of the error
    #     error_text = "<p>The error:<br>" + str(e) + "</p>"
    #     hed = '<h1>Something is broken.</h1>'
    #     return hed + error_text

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
