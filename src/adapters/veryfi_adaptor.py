from veryfi import Client
import os

def veryfi_adaptor():
    client_id = os.getenv('VERYFI_CLIENT_ID')
    client_secret = os.getenv('VERYFI_CLIENT_SECRET')
    username = os.getenv('VERYFI_USERNAME')
    api_key = os.getenv('VERYFI_API_KEY')

    # categories = ['Grocery', 'Utilities', 'Travel']
    files = os.listdir('./data/receipts')
    data_path = "./data/receipts/"
    print(f"files = {files}")
    # file_path = './data/broken.jpg'

    # This submits document for processing (takes 3-5 seconds to get response)
    veryfi_client = Client(client_id, client_secret, username, api_key)
    receipt_items = []
    for file in files:
        response = veryfi_client.process_document(data_path + file)
        print("response from veryfi: ", response)

        items = []
        line_items = response['line_items']
        for item in line_items:
            print(f"item = {item}")
            item_description = item['description']
            items.append(item_description)

        receipt_items.append(items)

    return receipt_items
