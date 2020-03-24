import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# El proceso base se saco de los Docs:
# https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet


def encrypt(password, file):

    """ Encripta el archivo dado por el usuario """

    salt = b'\xbd\x10\xcb\x8aK\x88Dw\xd8\x1b!\x909.\x07e'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  # Convierte la contraseña dada en los parametros a una segura
    f = Fernet(key)
    with open(file, 'r') as file_encryption:
        text_from_file = file_encryption.read().encode()  # Lee el archivo y convierte el string a bytes
        EncryptedToken = f.encrypt(text_from_file)  # Encripta los bytes creados arriba
        file_encryption.close()
    return EncryptedToken


def decrypt(password, token):

    """ Desencripta el archivo dado por el usuario """

    salt = b'\xbd\x10\xcb\x8aK\x88Dw\xd8\x1b!\x909.\x07e'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  # Convierte la contraseña dada en los parametros a una segura
    f = Fernet(key)
    DecryptedToken = f.decrypt(token)  # Desencripta el archivo dado
    return DecryptedToken
