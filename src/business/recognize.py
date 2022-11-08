from adapters import mindee_adapter, veryfi_adapter
import configs.app_config as app_config
from db.models.items import Items
from db.db_instance import db


def recognize():
    print("recognizing ...")

    if app_config.OCR_ENGINE_SUPPLIER == "VERYFI":  # TODO: move "VERYFI" as enum
        items = veryfi_adapter()
        print(f"recognized items = {items}")

        # save to database
        item = Items(name="Test", price=1.2, quantity=1, vendor="Test Vendor")
        db.session.add(item)
        db.session.commit()

        return items
    else:
        mindee_adapter()
