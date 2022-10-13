import os
from mindee import Client

def mindee_adaptor():
    # Note that the latest version of the API will be called
    api_key = os.getenv('RECEIPT_OCR_API_KEY')

    receipt_ocr_client = Client().config_receipt(api_key)

    receipt_doc = receipt_ocr_client.doc_from_path("./data/1.jpg")
    parsed_receipt = receipt_doc.parse("receipt")
    response_code = parsed_receipt.http_response.api_request.status_code
    parsed_receipt.document_type.prediction # content is in the prediction section

