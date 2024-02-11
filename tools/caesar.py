"""Caesar rot13 Tool"""
def rot13(text):
    """Krypterar och dekrypterar rot13 chiffer"""
    result = ""
    for char in text:
        if char.isalpha():  # Only rotate letters
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + 13) % 26 + start)
        else:
            result += char  # Non-alphabetic characters are not changed
    # Define the 'crypto13' variable with the text you want to encrypt


    # Pass the 'crypto13' variable to the ROT13 function
    #encrypted_text = rot13(text)
    print("Krypterad text:", result)

    # Since ROT13 is its own inverse, decrypting the encrypted text will yield the original text
   # decrypted_text = rot13(encrypted_text)
    print("Dekrypterad text:", text)
    return result
