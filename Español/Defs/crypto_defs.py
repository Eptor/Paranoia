import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#! El proceso base se saco de los Docs: https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet

def encrypt(password, file):
    salt = b'\xbd\x10\xcb\x8aK\x88Dw\xd8\x1b!\x909.\x07e'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password)) # Convierte la contraseña dada en los parametros a una segura
    f = Fernet(key)
    with open(file, 'r') as file:
        text_from_file = file.read().encode() # Lee el archivo y convierte el string a bytes
        EncryptedToken = f.encrypt(text_from_file) # Encripta los bytes creados arriba
        file.close()
    return EncryptedToken


def decrypt(password, token):
    salt = b'\xbd\x10\xcb\x8aK\x88Dw\xd8\x1b!\x909.\x07e'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password)) # Convierte la contraseña dada en los parametros a una segura
    f = Fernet(key)
    DecryptedToken = f.decrypt(token) # Desencripta el archivo dado
    return DecryptedToken
