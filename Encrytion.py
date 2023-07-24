import string
import random
# Ascii_letters
chars = " " + string.ascii_letters + string.digits 
chars = list(chars)
#Key 
key = chars.copy()
random.shuffle(key)

#Encryption Massage -->
encrypted = input('Enter a message to encrypt: ')
decrypted = ''

for i in encrypted:
    index = chars.index(i)
    decrypted += key[index]

print(f'Original massage {encrypted}')
print(f'Encryt massage: {decrypted}')

#Decryption Massage -->

decrypted = input('Enter a message to decrypt: ')
encrypted = ''

for x in decrypted:
    index = key.index(x)
    encrypted += chars[index]

print(f'Encrypt massage {decrypted}')
print(f'Original massage {encrypted}')