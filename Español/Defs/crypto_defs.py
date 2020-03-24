import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# El proceso base se saco de los Docs:
# https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet


def encrypt(password, mode, data):

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
    if mode == 1:
        with open(data, 'r') as file_encryption:
            # Reads the file and turns the string into bytes
            text_from_file = file_encryption.read().encode()
            # Encrypts the bytes grabbed above
            EncryptedToken = f.encrypt(text_from_file)
            file_encryption.close()
    elif mode == 2:
        EncryptedToken = f.encrypt(data)
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
