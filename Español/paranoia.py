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
    # Encripta archivo
    if sys.argv[1] == "-F" and sys.argv[2] == "-e" and sys.argv[3] != "":
        # Convierte la ruta dada a ruta de windows
        file = Path(input("Archivo a encriptar (usa la ruta completa si es necesario)\n> "))
        # Agarra la contraseña y la convierte en bytes
        password = sys.argv[3].encode()
        sleep(1)
        print("Iniciando...")
        EncryptedToken = defs.encrypt(password, 1, file)
        # Agarra la ruta del archivo original para crear el nuevo archivo
        file_name = path.dirname(path.abspath(file)) + "\encrypted.file"

        with open(file_name, "wb") as file_encryption:
            file_encryption.write(EncryptedToken)  # Escribe el archivo encriptado
            file_encryption.close()

        print("Completado.")
        system("cls")

    # Desencripta archivo
    elif sys.argv[1] == "-F" and sys.argv[2] == "-d" and sys.argv[3] != "":
        file = input("Archivo a desencriptar (usa la ruta completa si es necesario)\n> ")
        file_name = input("Nombre del nuevo archivo (incluye extension - No uses ruta completa)\n> ")
        # Agarra la ruta del archivo original para crear el nuevo archivo
        file_name = f"{path.dirname(path.abspath(file))}\{file_name}"
        # Agarra la contraseña y la convierte en bytes
        password = sys.argv[3].encode()
        sleep(1)
        print("Iniciando...")

        with open(file, "r") as file_encrypted:
            # Lee el archivo y convierte el string en bytes
            token = file_encrypted.read().encode()
            DecryptedToken = defs.decrypt(
                password, token)  # Desencripta el archivo
            file_encrypted.close()

        with open(file_name, "wb") as final_file:  # Crea el archivo desencriptado
            final_file.write(DecryptedToken)  # Escribe el archivo desencriptado
            final_file.close()

        print("Completado.")
        system("cls")

    # Encripta texto
    elif sys.argv[1] == "-T" and sys.argv[2] == "-e" and sys.argv[3] != "":
        # Turns the string given into bytes
        data = input("Que quieres encriptar?\n> ").encode()
        # Agarra la contraseña y la convierte a bytes
        password = sys.argv[3].encode()
        EncryptedToken = defs.encrypt(password, 2, data)  # Encripta el texto
        pyperclip.copy(EncryptedToken.decode())
        print(Fore.GREEN + """
        Tu texto ha sido encriptado y copiado a tu portapapeles.""")
        sleep(2)
        system("cls")

    elif sys.argv[1] == "-T" and sys.argv[2] == "-d" and sys.argv[3] != "":
        data = input("Que quieres desencriptar?\n> ").encode()
        password = sys.argv[3].encode()  # Agarra la contraseña y la convierte a bytes
        DecryptedToken = defs.decrypt(password, data)  # Desencripta el texto
        print(f"""
        Tu texto desencriptado es: {Fore.GREEN + DecryptedToken.decode()}
        {Fore.RESET + "Y ha sido copiado a tu portapapeles"}.""")  # Convierte los bytes a string para poder concatenarlos con Fore
        pyperclip.copy(DecryptedToken.decode())
        sleep(2)
        system("cls")

# Error handle
else:
    print('''
    Puedes usar -F para usar el modo de archivos o usar -T para el modo de texto, luego:
    Puedes usar "-e" + tu contraseña para encriptar (paranoia.py 'e password123)
    Puedes usar "-d" + tu contraseña para desencriptar (paranoia.py -d password123)
    Puedes usar "-h" para ver este mensaje
''')
