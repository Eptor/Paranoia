# Native modules
import sys
from os import system
from time import sleep
from pathlib import Path

# Local import
import Defs.crypto_defs as defs

if len(sys.argv) == 3:
    # Encrypt
    if sys.argv[1] == "-e" and sys.argv != "":
        file = Path(input("File name (use full path if necessary)\n> ")) # Turns the given file name to a windows path
        password = sys.argv[2].encode() # Gets the password and turns it to bytes
        sleep(1)
        print("Starting...")
        EncryptedToken = defs.encrypt(password, file)
        with open("encrypted.file", "wb") as file_encryption:
            file_encryption.write(EncryptedToken)
            file_encryption.close()
        print("Procces completed.")
        system("cls")
    # Decrypt
    elif sys.argv[1] == "-d" and sys.argv[2] != "":
        file = input("File name (use full path if necessary)\n> ")
        password = sys.argv[2].encode() # Gets the password and turns it to bytes
        sleep(1)
        print("Starting...")
        with open(file, "r") as file_encrypted:
            token = file_encrypted.read().encode() # Reads the file and convert the string to bytes
            DecryptedToken = defs.decrypt(password, token) # Decryption of the file
            file_encrypted.close()
        with open("decrypted.file", "wb") as final_file: # Creates the decrypted file
            final_file.write(DecryptedToken)
            final_file.close()
        print("Procces completed.")
        system("cls")

#! Error handle
elif len(sys.argv) < 3:
    print("It's necessary that you use the 2 parameters")
elif len(sys.argv) > 3:
    print("You used more than 2 parameters")
else:
    print("An error has occured")
