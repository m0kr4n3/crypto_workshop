from Crypto.Util.number import inverse

p = 3
q = 11 
n = p*q

phi = (p-1) * (q-1)
e=3
d=inverse(phi,e)

print(f"Public key : {(n,e)}    |Private key : {(n,d)}")

msg=31
enc=(msg**e)%n

dec=(enc**d)%n

print(f"RSA_encrypt({msg}) = {enc}\nRSA_decrypt({enc}) = {dec}")