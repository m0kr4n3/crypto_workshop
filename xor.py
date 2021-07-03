from binascii import unhexlify

enc="0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

prefix="crypto{a"

'''
A ^ B = C

B = A ^ C

'''

unhex_enc=unhexlify(enc).decode()

keys=[]
for i in range(len(prefix)):
    keys.append(ord(prefix[i])^ord(unhex_enc[i]))

print(keys)

flag=""
for i in range(len(unhex_enc)):
    flag+=chr(ord(unhex_enc[i])^keys[i%len(keys)])

print(flag)
