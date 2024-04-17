import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# Encriptação
plain_text = input('Texto para encriptar: ')
cipher_text = ''

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
    
print(f'{cipher_text}')

# Dencriptação
cipher_text = input('Texto para dencriptar: ')
plain_text = ''

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
    
print(f'{plain_text}')