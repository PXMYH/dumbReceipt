from .models import db, Product


def connect_database(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///receipt.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    with app.app_context():
        try:
            db.init_app(app)
            db.create_all()
            products = Product.query.all()
            print(f"Products: {products}")
        except Exception as e:
            raise ConnectionError(f"Connection to database failed, {e}")
