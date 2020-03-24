# Native modules
import sys
from os import system, path
from time import sleep
from pathlib import Path

# Local import
import Defs.crypto_defs as defs

if len(sys.argv) == 3:
    # Encrypt
    if sys.argv[1] == "-e" and sys.argv != "":
        file = Path(input("File to encrypt (use full path if necessary)\n> "))  # Turns the given file name to a windows path
        password = sys.argv[2].encode()  # Gets the password and turns it to bytes
        sleep(1)
        print("Starting...")
        EncryptedToken = defs.encrypt(password, file)
        file_name = path.dirname(path.abspath(file)) + "\encrypted.file"  # Gets the path of the file and creates the new one in there

        with open(file_name, "wb") as file_encryption:
            file_encryption.write(EncryptedToken)  # Writes the encrypted file
            file_encryption.close()

        print("Procces completed.")
        system("cls")
        
    # Decrypt
    elif sys.argv[1] == "-d" and sys.argv[2] != "":
        file = input("File to decrypt (use full path if necessary)\n> ")
        file_name = input("New file name (include extension - Dont use full path)\n> ")
        file_name = f"{path.dirname(path.abspath(file))}\{file_name}"  # Gets the path of the file and add the given name
        password = sys.argv[2].encode()  # Gets the password and turns it to bytes
        sleep(1)
        print("Starting...")

        with open(file, "r") as file_encrypted:
            token = file_encrypted.read().encode()  # Reads the file and convert the string to bytes
            DecryptedToken = defs.decrypt(password, token)  # Decryption of the file
            file_encrypted.close()

        with open(file_name, "wb") as final_file:  # Creates the decrypted file
            final_file.write(DecryptedToken)  # Writes the decrypted file
            final_file.close()

        print("Procces completed.")
        system("cls")

# Error handle
elif len(sys.argv) == 2 and sys.argv[1] == "-h" or len(sys.argv) < 2:
    print('''
    You can use "-e" + your password to enctypr (paranoia.py -e password123)
    You can use "-d" + your password to decrypt (paranoia.py -d password123)
    You can use "-h" to show this message
''')
elif len(sys.argv) > 3:
    print("You used more than 2 parameters")
