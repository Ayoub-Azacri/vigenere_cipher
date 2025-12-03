
# chifferement
import string
text = "lapin"
key = 3_000_000
def cesar_cipher(text, key, cipher = True):

    key = key if cipher  else -key # ternay

    list_of_crypted_chars = ""
    for char in text:
        # find position of char ascii and add a décalage
        crypted_char = chr((ord(char) + key) % 1_114_112)
        list_of_crypted_chars += crypted_char
    return " ".join(list_of_crypted_chars)

#* Cette fonctiona va overflow la mémoire ram, fonctionne mais pas efficiant
#* Au lieu de faire += on fait List_of_crypted_chars.append(crypted_char)
#* return "".join(List_of_crypted_chars)

# dechiffrement par force brute
def brute_force_crypted_text(crypted_text):
    for potential_key in range(1, 1_114_112):
        potential_initial_text = cesar_cipher(crypted_text, potential_key, cipher = False)

        for char in potential_initial_text:
            if char in string.printable:
                print(potential_key)
                print(potential_initial_text)
                print("-----")
                break


# chiffrement vigenere
def vigenere_cipher(text, password, cipher = True):
    #?convert password to list of keys
    list_of_keys = [ord(char) for char in password]
    crypted_text = ""
    #chiffre char by char
    for index, char in enumerate(text):
        current_key = list_of_keys[index % len(list_of_keys)]
        crypted_char = cesar_cipher(text=char, key=current_key, cipher=cipher)
        crypted_text += crypted_char

    return crypted_text




#crypted_text = cesar_cipher(text, key)
#initial_text = cesar_cipher(text=crypted_text,key = 3_000_000, cipher = False)
#print(f"Given text:{initial_text}")
#print(f"Crypted text: {crypted_text}")

#brute_force_crypted_text(crypted_text)


crypted_text = vigenere_cipher(text="Bonjour tout le monde !", password="Azerty12345")
print(crypted_text)

initial_text = vigenere_cipher(text=crypted_text, password="Azerty12345", cipher=False)
print(initial_text)