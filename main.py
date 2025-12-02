
# chifferement
text = "lapin"
key = 3
def cesar_cipher(text, key):
    crypted_text = ""
    for char in text:
        # find position of char ascii and add a décalage
        crypted_char = chr((ord(char) + key))
        crypted_text += crypted_char
    return crypted_text

print(f"Given text: {text}")
crypted_text = cesar_cipher(text,key)
print(f"Crypted text: {crypted_text}")

#déchifferement
def dechiffre_cesar(text, key):
    decrypted_text = ""
    for char in text:
        # find position of char ascii and remove the décalage
        decrypted_char = chr((ord(char) - key))
        decrypted_text += decrypted_char
    return decrypted_text

decrypted_text = dechiffre_cesar(crypted_text, key)
print(f"Deccrypted text: {decrypted_text}")

