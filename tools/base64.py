import base64

def auto_encode_decode(input_string):
    try:
        # Försök att dekodera strängen från Base64
        decoded_bytes = base64.b64decode(input_string, validate=True)
        # Kontrollera om dekodningen resulterade i en läsbar sträng
        decoded_string = decoded_bytes.decode('utf-8')
        print(f"Detektion: Strängen var Base64-kodad.")
        print(f"Dekodad sträng: {decoded_string}")
    except (ValueError, UnicodeDecodeError):
        # Om dekodningen misslyckas, anta att strängen är i klartext och kodas till Base64
        encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
        encoded_string = encoded_bytes.decode('utf-8')
        print(f"Detektion: Strängen var i klartext.")
        print(f"Kodad till Base64: {encoded_string}")
