import os
from mindee import Client


class MindeeAdapter:
    def __init__(self):
        # Note that the latest version of the API will be called
        self.api_key = os.getenv("MINDEE_API_KEY")

        self.client = Client().config_receipt(self.api_key)

    def process_documents(self):
        receipt_doc = self.client.doc_from_path("./data/1.jpg")
        parsed_receipt = receipt_doc.parse("receipt")
        response_code = parsed_receipt.http_response.api_request.status_code
        parsed_receipt.document_type.prediction  # content is in the prediction section
