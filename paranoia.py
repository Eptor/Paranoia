# Native modules
import sys
from os import system, path
from time import sleep
from pathlib import Path

# Local import
import Defs.crypto_defs as defs

# Installed modules
import pyperclip
from colorama import Fore, init

init(autoreset=True)

if len(sys.argv) == 4:
    # Encrypt
    if sys.argv[1] == "-F" and sys.argv[2] == "-e" and sys.argv[3] != "":
        file = Path(input("File to encrypt (use full path if necessary)\n> "))  # Turns the given file name to a windows path
        password = sys.argv[3].encode()  # Gets the password and turns it to bytes
        sleep(1)
        print("Starting...")
        EncryptedToken = defs.encrypt(password, 1, file)
        file_name = path.dirname(path.abspath(file)) + "\encrypted.file"  # Gets the path of the file and creates the new one in there

        with open(file_name, "wb") as file_encryption:
            file_encryption.write(EncryptedToken)  # Writes the encrypted file
            file_encryption.close()

        print(Fore.CYAN + "Procces completed.")
        system("cls")

    # Decrypt
    elif sys.argv[1] == "-F" and sys.argv[2] == "-d" and sys.argv[3] != "":
        file = input("File to decrypt (use full path if necessary)\n> ")
        file_name = input("New file name (include extension - Dont use full path)\n> ")
        file_name = f"{path.dirname(path.abspath(file))}\{file_name}"  # Gets the path of the file and add the given name
        password = sys.argv[3].encode()  # Gets the password and turns it to bytes
        sleep(1)
        print("Starting...")

        with open(file, "r") as file_encrypted:
            token = file_encrypted.read().encode()  # Reads the file and convert the string to bytes
            DecryptedToken = defs.decrypt(password, token)  # Decryption of the file
            file_encrypted.close()

        with open(file_name, "wb") as final_file:  # Creates the decrypted file
            final_file.write(DecryptedToken)  # Writes the decrypted file
            final_file.close()

        print(Fore.CYAN + "Procces completed.")
        system("cls")

    elif sys.argv[1] == "-T" and sys.argv[2] == "-e" and sys.argv[3] != "":
        data = input("What do you want to encrtpy?\n> ").encode()  # Turns the string given into bytes
        password = sys.argv[3].encode()  # Grabs the password and turns it into bytes
        EncryptedToken = defs.encrypt(password, 2, data)  # Encrypts the data
        pyperclip.copy(EncryptedToken.decode())
        print(Fore.GREEN + """
        Your data has been encrypted and copied to your clipboard.""")
        sleep(2)
        system("cls")

    elif sys.argv[1] == "-T" and sys.argv[2] == "-d" and sys.argv[3] != "":
        data = input("What do you want to decrypt?\n> ").encode()
        password = sys.argv[3].encode()  # Gets the password and turns it to bytes 
        DecryptedToken = defs.decrypt(password, data)  # Decrypts the data
        print(f"""
        Your decrypted data is: {Fore.GREEN + DecryptedToken.decode()} 
        {Fore.RESET + "And it has been copied to your clipboard"}.""")  # Turns the bytes to string so it can concatenate with Fore
        pyperclip.copy(DecryptedToken.decode())
        sleep(2)
        system("cls")

# Error handle
else:
    print('''
    You can use -F to use the Files mode or use -T for Text mode, then:
    You can use "-e" + your password to enctypr (paranoia.py -e password123)
    You can use "-d" + your password to decrypt (paranoia.py -d password123)
    You can use "-h" to show this message
''')
