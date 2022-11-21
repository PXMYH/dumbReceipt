from veryfi import Client
import os
import configs.app_config as app_config


def veryfi_adaptor():
    client_id = os.getenv("VERYFI_CLIENT_ID")
    client_secret = os.getenv("VERYFI_CLIENT_SECRET")
    username = os.getenv("VERYFI_USERNAME")
    api_key = os.getenv("VERYFI_API_KEY")

    # categories = ['Grocery', 'Utilities', 'Travel']
    # RECEIPT_FILE_DIR = "./uploads/receipts"
    files = os.listdir(app_config.RECEIPT_FILE_DIR)
    print(f"files = {files}")

    # This submits document for processing (takes 3-5 seconds to get response)
    veryfi_client = Client(client_id, client_secret, username, api_key)
    receipt_items = []
    for file in files:
        response = veryfi_client.process_document(
            app_config.RECEIPT_FILE_DIR + "/" + file
        )
        print("response from veryfi: ", response)

        items = []
        line_items = response["line_items"]
        for item in line_items:
            print(f"item = {item}")
            item_description = item["description"]
            items.append(item_description)

        # convert to data models

        receipt_items.append(items)

    return receipt_items
