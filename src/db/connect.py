from .models import db, Product


def connect_database(app):
    db_name = "receipt.db"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_name
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)

    try:
        with app.app_context():
            products = Product.query.all()
            print(f"Products: {products}")
    except Exception as e:
        raise ConnectionError(f"Connection to database failed, {e}")
