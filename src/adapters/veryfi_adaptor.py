from veryfi import Client

def veryfi_adaptor():
    client_id = 'vrf15ZdGoEPHl42p3oBoRruJe5ruTnrUiKXawYz'
    client_secret = 'ikZ0POOxZi9LfTjGkm3wp2lV1uNGDK3PRfp21J27IcIhs3frjwKHzO8BxKnx05HlunXLelljEiknnO59axdSHhhuCXN945KsTFIsB951SF0K3jzewRNRwZHOSyLAEZmm'
    username = 'pxmyhdev'
    api_key = '5de47e916c47c26cd51d15f694a19af9'

    # categories = ['Grocery', 'Utilities', 'Travel']
    file_path = './data/broken.jpg'

    # This submits document for processing (takes 3-5 seconds to get response)
    veryfi_client = Client(client_id, client_secret, username, api_key)
    response = veryfi_client.process_document(file_path)
    print("response from veryfi: ", response)
