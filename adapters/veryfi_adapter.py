from veryfi import Client
import os
import configs.app_config as app_config
import json


def veryfi_adapter():
    client_id = os.getenv("VERYFI_CLIENT_ID")
    client_secret = os.getenv("VERYFI_CLIENT_SECRET")
    username = os.getenv("VERYFI_USERNAME")
    api_key = os.getenv("VERYFI_API_KEY")

    is_debug = app_config.DEBUG_ENABLED

    receipt_dir = os.path.join(
        os.path.dirname(__file__), "..", app_config.RECEIPT_FILE_DIR
    )
    print(f"veryfi receipt directory: {receipt_dir}")

    if is_debug:
        # debug mode enabled, use dummy file for response
        with open("stubs/costco.json", "r") as f:
            response = json.load(f)
    else:
        # real mode enabled, use verify and count towards API usage
        # this submits document for processing (takes 3-5 seconds to get response)
        veryfi_client = Client(client_id, client_secret, username, api_key)

    files = [file for file in os.listdir(receipt_dir) if not file.endswith(".gitkeep")]
    print(f"files = {files}")

    receipt_items = []

    for file in files:
        if not is_debug:
            print(f"Execution mode, real API call is executed for {file}.")
            response = veryfi_client.process_document(os.path.join(receipt_dir, file))
            print("response from veryfi: ", response)

        item_metadata = [
            response["created_date"],
            response["category"],
            response["currency_code"],
            response["subtotal"],
            response["tax_lines"][0]["total"] if response["tax_lines"] else "None",
            response["tax_lines"][0]["name"] if response["tax_lines"] else "None",
            response["tax_lines"][0]["rate"] if response["tax_lines"] else "None",
            response["vendor"]["name"],
            response["vendor"]["category"],
            response["vendor"]["address"],
            response["vendor"]["type"],
        ]

        line_items = response["line_items"]
        for line_item in line_items:
            item = item_metadata + [line_item["description"], line_item["quantity"]]
            print(f"item = {item}")
            receipt_items.append(item)

    return receipt_items
