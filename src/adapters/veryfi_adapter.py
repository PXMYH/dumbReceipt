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
    # veryfi_client = Client(client_id, client_secret, username, api_key)
    receipt_items = []
    for file in files:
        # response = veryfi_client.process_document(RECEIPT_FILE_DIR + "/" + file)
        # print("response from veryfi: ", response)

        import json

        with open("winners.json", "r") as f:
            response = json.load(f)
        # response = "{'account_number': '411589', 'bill_to': {'address': None, 'name': None, 'parsed_address': None, 'vat_number': None}, 'cashback': None, 'category': 'Job Supplies', 'created_date': '2022-11-26 05:18:04', 'currency_code': 'CAD', 'date': '2020-11-14 14:05:56', 'delivery_date': None, 'discount': None, 'document_reference_number': '111420140550', 'document_title': None, 'document_type': 'receipt', 'due_date': None, 'duplicate_of': 103805863, 'external_id': None, 'id': 104764178, 'img_file_name': '104764178.pdf', 'img_thumbnail_url': 'https://scdn.veryfi.com/receipts/ad1784bd-b92a-4c55-be08-9f87955d4835/thumbnail.jpg?Expires=1669440785&Signature=FZrvnfIoLIye0654O1Na5fZwjws0ewMZsSEq8z3wwySMwWsPCSMFNvYjPZUJn4SHWSKRY3qYHSm32gkWqjQ08Cs~eGXa74lB0pxmewetNuAIaDyS98cfdE1xDk5M0V6kDto7mMd83JQNTMGJ~mgkyv1zae8YgVrgzaz26bN37PVx1sWMTMk3rA0b0Ar5PRWXXxM7GfUP0rPRBesJzyrOJn74DRUDyCVo7c9W9WWQYim2Jt3UAHwwdwza0~S-cvzWEn6DeRafDN-lCv2stFtdJqhwf~nGY2dfOMDwS-3BgOiZScZrYXzty3p-w7HH~v~15VeqWEfeQzsKIQs1iuVSWw__&Key-Pair-Id=APKAJCILBXEJFZF4DCHQ', 'img_url': 'https://scdn.veryfi.com/receipts/ad1784bd-b92a-4c55-be08-9f87955d4835/38bb6d94-729e-405e-bdaf-7f22448972ed.pdf?Expires=1669440785&Signature=fzlEGCSqhtMlceNlIt1EmTnDxnS0cE8mYM5a5SifvGqc5yn2Qmh6TVVhXXup73111lNvOLaacJeoY6~num6UBEl5OXAOqZJ~1Sst5VSWhzRr7q04GZjh8aCR5aQu~xp0OrhrKU796jFdaY0BFBCiKznXPSlWXgWmFTRiQkfE0ycq0JNApkv5-Rj9IT2z1jAomTbB5wHvl7wUq4L2fPlfv5W2zPjntM5ylIH0oa0-x5ZBLqLghhsLkczGg4iL9fJ7EqbsTiA0qqugv-zjVvJ9~lKHYMshxhR~NGeUWfTjw-B6-rgNGrE00vrNOqWR6NUTShxuggZpgPK-OqH8uZvM6w__&Key-Pair-Id=APKAJCILBXEJFZF4DCHQ', 'insurance': None, 'invoice_number': '90282013350185803', 'is_duplicate': True, 'is_money_in': False, 'line_items': [{'date': None, 'description': '86-STORAGE/FRAME', 'discount': None, 'discount_rate': None, 'end_date': None, 'id': 399426450, 'order': 0, 'price': None, 'quantity': 1.0, 'reference': None, 'section': None, 'sku': '027408', 'start_date': None, 'tags': [], 'tax': None, 'tax_rate': None, 'text': '86-STORAGE/FRAME 027408\t$29.99 H', 'total': 29.99, 'type': 'food', 'unit_of_measure': None, 'upc': None}], 'meta': {'owner': 'pxmyhdev'}, 'notes': None, 'ocr_text': \"WINNERS\n\nWOODBINE & HWY 7\n3105 HIGHWAY #7\nMARKHAM, ON L3R 0J5\nCanada\n905-513-8464\nGST NO.86032 6255 RT0001CA #07043\n\nREGULAR SALE\n86-STORAGE/FRAME 027408\t$29.99 H\nSubtotal\t\t\t$29.99\nON HST 13.000%\t\t$3.90\n\nTotal\t\t\t$33.89\neGift Card\t\t$20.00\n****** *******1279\nEntry Method: Scanned\nBalance: $0.00\nAuth #: 002000\nReference Number: 111420140550\nVISA\t\t\t$13.89\nTRANSACTION RECORD\nTrans# 203350\nCard #:\t\t************0247\nCard Entry: TAP CHIP\tAccount:VISA\nTrans:PURCHASE\tAmount: $13.89\nAuth #:411589\tSequence #:000030\nTerm ID:\t\t\t001\nDate:20/11/14\tTime:14:05:56\nApproved\nApplication Label: Visa CREDIT\nTVR: 0000000000\nAID: A0000000031010\nTC: 31BDF60C4ECE5745\nChange\t\t\t$0.00\n\t*********:\nReceipt ID:90282013350185803\n\n\t********\nWE VALUE YOUR FEEDBACK\nRESPOND BY 21/11/20 to get 10\nCHANCES to WIN $1000 DAILY PLUS\n1 chance to WIN 1 OF 3 $500 prizes\nWEEKLY just by providing your\nreview at www.tjxcanada-opinion.ca\nJurisdiction may req skill test.\nSee website for complete rules,\neligibility, sweepstakes period\n& PREVIOUS winners. No purchase/\nsurvey needed to enter. Sponsored\nby Empathica Inc. across multiple\nint'l clients. Survey#0282013350\n******\nSold Item Count = 1\nOT11314CKD113117XT4ATFP40\n40282 1 3350 14/11/2020 14:05:34\t1040\nCustomer Copy\nReturns with receipts for purchases from\nNov. 02 to Dec. 24 accepted until\nJan. 08/21. Returns w/ gift receipts\nvalid for gift card only. See Holiday\nReturn Policy in store for full details\n\tScanned with CamScanner", 'order_date': None, 'payment': {'card_number': '0247', 'display_name': 'Visa ***0247', 'terms': None, 'type': 'visa'}, 'pdf_url': 'https://scdn.veryfi.com/receipts/ad1784bd-b92a-4c55-be08-9f87955d4835/38bb6d94-729e-405e-bdaf-7f22448972ed.pdf?Expires=1669440785&Signature=fzlEGCSqhtMlceNlIt1EmTnDxnS0cE8mYM5a5SifvGqc5yn2Qmh6TVVhXXup73111lNvOLaacJeoY6~num6UBEl5OXAOqZJ~1Sst5VSWhzRr7q04GZjh8aCR5aQu~xp0OrhrKU796jFdaY0BFBCiKznXPSlWXgWmFTRiQkfE0ycq0JNApkv5-Rj9IT2z1jAomTbB5wHvl7wUq4L2fPlfv5W2zPjntM5ylIH0oa0-x5ZBLqLghhsLkczGg4iL9fJ7EqbsTiA0qqugv-zjVvJ9~lKHYMshxhR~NGeUWfTjw-B6-rgNGrE00vrNOqWR6NUTShxuggZpgPK-OqH8uZvM6w__&Key-Pair-Id=APKAJCILBXEJFZF4DCHQ', 'purchase_order_number': 'None', 'reference_number': 'VIGHG-4178', 'rounding': 'None', 'service_end_date': 'None', 'service_start_date': 'None', 'ship_date': 'None', 'ship_to': {'address': 'None', 'name': 'None', 'parsed_address': 'None'}, 'shipping': 'None', 'store_number': 'None', 'subtotal': 29.99, 'tax': 3.9, 'tax_lines': [{'base': 'None', 'name': 'ON HST', 'order': 0, 'rate': 13.0, 'total': 3.9}], 'tip': 'None', 'total': 33.89, 'total_weight': 'None', 'tracking_number': 'None', 'updated_date': '2022-11-26 05:18:05', 'vendor': {'abn_number': 'None', 'account_number': 'None', 'address': '3105 Highway 7, Markham, ON L3R 0T9, Canada', 'bank_name': 'None', 'bank_number': 'None', 'bank_swift': 'None', 'category': 'discount store', 'email': 'None', 'fax_number': 'None', 'iban': 'None', 'lat': 43.8479965809757, 'lng': -79.3537330357364, 'logo': 'https://cdn.veryfi.com/logos/us/330773943.jpg', 'name': 'Winners', 'phone_number': '905-513-8464', 'raw_address': '3105 HIGHWAY #7\nMARKHAM, ON L3R 0J5\nCanada', 'raw_name': 'Winners', 'reg_number': 'None', 'type': 'discount store', 'vat_number': '86032 6255 RT0001CA', 'web': 'None'}"

        items = []

        # TODO: bad data representation, but for now, get the skeleton working

        # metadata
        category = response["category"]
        currency = response["currency_code"]
        date = response["created_date"]

        # total amount
        total = response["subtotal"]

        # tax
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
        items.append(date)
        items.append(category)
        items.append(currency)
        items.append(total)
        items.append(tax_amount)
        items.append(tax_name)
        items.append(tax_rate)
        items.append(vendor_name)
        items.append(vendor_category)
        items.append(vendor_address)
        items.append(vendor_type)

        line_items = response["line_items"]
        for item in line_items:
            print(f"item = {item}")
            item_description = item["description"]
            item_quantity = item["quantity"]
            items.append(item_description)
            items.append(item_quantity)

        receipt_items.append(items)

    return receipt_items
