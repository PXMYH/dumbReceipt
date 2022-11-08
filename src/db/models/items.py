from db.db_instance import db
from sqlalchemy.sql import func

# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# identify all columns by name and data type
class Items(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float, nullable=False)
    vendor = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, name, quantity, price, vendor):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.vendor = vendor

    def __repr__(self):
        return f"<{self.quantity} item(s) {self.name} purchased at {self.price} from {self.vendor}>"
