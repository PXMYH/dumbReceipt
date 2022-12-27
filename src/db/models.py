from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
print("connecting to db")


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    vendor = db.Column(db.String(80))
    created_at = db.Column(db.DateTime)

    def __repr__(self):
        return (
            f"<Product {self.id}: name={self.name} "
            f"quantity={self.quantity} price={self.price} "
            f"vendor={self.vendor} created_at={self.created_at}>"
        )
