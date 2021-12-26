from cryptography.fernet import Fernet, MultiFernet
import pickle
import json

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64
import os

key = Fernet.generate_key()
print(key)
with open("fernet.key","rb") as file:
    f = Fernet(file.read())
print(f)

with open("fernet.key","wb") as file:
    file.write(key)

plaintext = bytes(json.dumps({"username":"admin","password":"password"}),encoding="utf-8")
ciphertext = f.encrypt(plaintext)
with open("details.txt","wb") as file:
    file.write(ciphertext)
print(plaintext,f.decrypt(ciphertext))

with open("details.txt","rb") as file:
    token = file.read()
print(f.decrypt(token))

message = b"Secret message!"
password = b"password"
key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())
f = MultiFernet([key1,key2])

salt = os.urandom(16)
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=390000)
key = base64.urlsafe_b64encode(kdf.derive(password))
f = Fernet(key)
print(salt)

token = f.encrypt(message)
print(token)
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=390000)
key = base64.urlsafe_b64encode(kdf.derive(b"password"))
f = Fernet(key)
print(f.decrypt(token))