from veryfi import Client
import os
import configs.app_config as app_config
import json


class VeryfiAdapter:
    def __init__(self):
        self.client_id = os.getenv("VERYFI_CLIENT_ID")
        self.client_secret = os.getenv("VERYFI_CLIENT_SECRET")
        self.username = os.getenv("VERYFI_USERNAME")
        self.api_key = os.getenv("VERYFI_API_KEY")

        self.is_debug = app_config.DEBUG_ENABLED

        self.receipt_dir = os.path.join(
            os.path.dirname(__file__), "..", app_config.RECEIPT_FILE_DIR
        )
        print(f"veryfi receipt directory: {self.receipt_dir}")

        if self.is_debug:
            # debug mode enabled, use dummy file for response
            with open("stubs/costco.json", "r") as f:
                self.response = json.load(f)
        else:
            # real mode enabled, use verify and count towards API usage
            # this submits document for processing (takes 3-5 seconds to get response)
            self.veryfi_client = Client(
                self.client_id, self.client_secret, self.username, self.api_key
            )

    def process_documents(self):
        files = [
            file
            for file in os.listdir(self.receipt_dir)
            if not file.endswith(".gitkeep")
        ]
        print(f"files = {files}")

        receipt_items = []

        for file in files:
            if not self.is_debug:
                print(f"Execution mode, real API call is executed for {file}.")
                response = self.veryfi_client.process_document(
                    os.path.join(self.receipt_dir, file)
                )
                print("response from veryfi: ", response)
            else:
                response = self.response

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
