from veryfi import Client
import os


def veryfi_adapter():
    client_id = os.getenv("VERYFI_CLIENT_ID")
    client_secret = os.getenv("VERYFI_CLIENT_SECRET")
    username = os.getenv("VERYFI_USERNAME")
    api_key = os.getenv("VERYFI_API_KEY")

    # categories = ['Grocery', 'Utilities', 'Travel']
    RECEIPT_FILE_DIR = "./uploads/receipts"
    files = [file for file in os.listdir(RECEIPT_FILE_DIR) if not ".gitkeep" in file]
    print(f"files = {files}")

    # This submits document for processing (takes 3-5 seconds to get response)
    veryfi_client = Client(client_id, client_secret, username, api_key)
    receipt_items = []
    for file in files:
        response = veryfi_client.process_document(RECEIPT_FILE_DIR + "/" + file)
        print("response from veryfi: ", response)

        # uncomment below 4 lines to test with dummy data
        # import json

        # with open("costco.json", "r") as f:
        #     response = json.load(f)

        item_metadata = []

        # TODO: bad data representation, but for now, get the skeleton working

        # metadata
        category = response["category"]
        currency = response["currency_code"]
        date = response["created_date"]

        # total amount
        total = response["subtotal"]

        # tax
        if len(response["tax_lines"]) == 0:
            print("The list is empty")
            tax_amount, tax_rate, tax_name = None, None, None
        else:
            print("tax = ", response["tax_lines"][0])
            tax_amount = response["tax_lines"][0]["total"]
            tax_rate = response["tax_lines"][0]["rate"]
            tax_name = response["tax_lines"][0]["name"]

        # vendor
        vendor_name = response["vendor"]["name"]
        vendor_address = response["vendor"]["address"]
        vendor_category = response["vendor"]["category"]
        vendor_type = response["vendor"]["type"]

        # record field order
        item_metadata.append(date)
        item_metadata.append(category)
        item_metadata.append(currency)
        item_metadata.append(total)
        item_metadata.append(tax_amount or "None")
        item_metadata.append(tax_name or "None")
        item_metadata.append(tax_rate or "None")
        item_metadata.append(vendor_name)
        item_metadata.append(vendor_category)
        item_metadata.append(vendor_address)
        item_metadata.append(vendor_type)

        line_items = response["line_items"]
        for line_item in line_items:
            item = []
            item_description = line_item["description"]
            item_quantity = line_item["quantity"]

            item.extend(item_metadata)
            item.append(item_description)
            item.append(item_quantity)
            print(f"item = {item}")
            receipt_items.append(item)

    return receipt_items
