from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os 

BLOCK_SIZE = 16

# key = os.urandom(16)
# iv = os.urandom(16)

key = b'A'*16
iv = b'B'*16

ecb = AES.new(key,AES.MODE_ECB)
cbc = AES.new(key,AES.MODE_CBC,iv)

plaintext = pad(b"whatever" ,BLOCK_SIZE)

pt_blocks = [plaintext[i:i+16] for i in range(0,len(plaintext),BLOCK_SIZE)]

ciphertext = cbc.encrypt(plaintext)

print(ciphertext)

# with open('aes.txt','wb') as w:
#     w.write(ciphertext)

ct_blocks = [ciphertext[i:i+16] for i in range(0,len(ciphertext),BLOCK_SIZE)]

# print(pt_blocks);input()

# print(ct_blocks);input()