from sqlalchemy.sql import text
from db.db_instance import db


def connect_database(app):
    try:
        with app.app_context():
            db.session.query(text("1")).from_statement(text("SELECT 1")).all()
    except Exception as e:
        raise ConnectionError(f"Connection to database failed, {e}")
