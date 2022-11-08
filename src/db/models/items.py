from db.db_instance import db

# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# identify all columns by name and data type
class Items(db.Model):
    __tablename__ = "socks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    vendor = db.Column(db.String)

    def __init__(self, name, quantity, price, vendor):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.vendor = vendor
