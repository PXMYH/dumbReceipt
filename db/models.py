from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
print("connecting to db")


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    vendor = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return (
            f"<Product {self.id}: name={self.name} "
            f"quantity={self.quantity} price={self.price} "
            f"vendor={self.vendor} created_at={self.created_at}>"
        )
