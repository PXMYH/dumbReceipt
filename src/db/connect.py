from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

def connect_database(app):
    db_name = 'receipt.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # this variable, db, will be used for all SQLAlchemy commands
    db = SQLAlchemy(app)
    print("connecting to db: " + db_name)

    try:
        with app.app_context():
            db.session.query(text('1')).from_statement(text('SELECT 1')).all()
    except Exception as e:
        raise ConnectionError(f"Connection to database failed, {e}")
