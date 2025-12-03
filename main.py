
# chifferement
text = "lapin"
key = 3
def cesar_cipher(text, key):
    crypted_text = ""
    for char in text:
        # find position of char ascii and add a décalage
        crypted_char = chr((ord(char) + key) % 1_114_112)
        crypted_text += crypted_char
    return crypted_text

print(f"Given text: {text}")
crypted_text = cesar_cipher(text,key)
print(f"Crypted text: {crypted_text}")