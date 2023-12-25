import hashlib

toHash = "admin"

hash = hashlib.sha256(toHash.encode()).hexdigest()

print(hash)

