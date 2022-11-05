from adapters.midee_adapter import mindee_adaptor
from adapters.veryfi_adaptor import veryfi_adaptor

import configs.app_config as app_config


def recognize():
    print("recognizing ...")

    mode = "VERYFI"

    if app_config.OCR_ENGINE_SUPPLIER == mode:
        items = veryfi_adaptor()
        print(f"recognized items = {items}")
        return items
    else:
        mindee_adaptor()
