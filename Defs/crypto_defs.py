import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# The base process was grabbed from the Docs:
# https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet


def encrypt(password, file):

    """ Encrypts the file given by the user """

    salt = b'\xbd\x10\xcb\x8aK\x88Dw\xd8\x1b!\x909.\x07e'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  # Generates a secure password using the given password in the parameters
    f = Fernet(key)
    with open(file, 'r') as file_encryption:
        text_from_file = file_encryption.read().encode()  # Reads the file and turns the string into bytes
        EncryptedToken = f.encrypt(text_from_file)  # Encrypts the bytes grabbed above
        file_encryption.close()
    return EncryptedToken


def decrypt(password, token):

    """ Decrypts the file given by the user """

    salt = b'\xbd\x10\xcb\x8aK\x88Dw\xd8\x1b!\x909.\x07e'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  # Generates a secure password using the given password in the parameters
    f = Fernet(key)
    DecryptedToken = f.decrypt(token)  # Decrypts the given file
    return DecryptedToken
