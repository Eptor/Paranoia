import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# The base process was grabbed from the Docs:
# https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet


def encrypt(password, mode, data):
    """ Encrypts the data given by the user """

    salt = b'\xbd\x10\xcb\x8aK\x88Dw\xd8\x1b!\x909.\x07e'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    # Generates a secure password using the given password in the parameters
    key = base64.urlsafe_b64encode(kdf.derive(password))
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
    """ Decrypts the data given by the user """

    salt = b'\xbd\x10\xcb\x8aK\x88Dw\xd8\x1b!\x909.\x07e'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    # Generates a secure password using the given password in the parameters
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    DecryptedToken = f.decrypt(token)  # Decrypts the given file
    return DecryptedToken
