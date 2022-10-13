from veryfi import Client
import os

def veryfi_adaptor():
    client_id = os.getenv('VERYFI_CLIENT_ID')
    client_secret = os.getenv('VERYFI_CLIENT_SECRET')
    username = os.getenv('VERYFI_USERNAME')
    api_key = os.getenv('VERYFI_API_KEY')

    # categories = ['Grocery', 'Utilities', 'Travel']
    file_path = './data/broken.jpg'

    # This submits document for processing (takes 3-5 seconds to get response)
    veryfi_client = Client(client_id, client_secret, username, api_key)
    response = veryfi_client.process_document(file_path)
    print("response from veryfi: ", response)
