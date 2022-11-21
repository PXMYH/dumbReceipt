from adapters.midee_adapter import mindee_adapter
from adapters.veryfi_adapter import veryfi_adapter

import configs.app_config as app_config


def recognize():
    print("recognizing ...")

    if app_config.OCR_ENGINE_SUPPLIER == "VERYFI":  # TODO: move "VERYFI" as enum
        items = veryfi_adapter()
        print(f"recognized items = {items}")
        return items
    else:
        mindee_adapter()
