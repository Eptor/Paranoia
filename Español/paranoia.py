# Native modules
import sys
import platform
from os import system, path
from time import sleep
from pathlib import Path
import datetime

# Local import
import Defs.crypto_defs as defs

# Installed modules
from colorama import Fore, init

init(autoreset=True)

if len(sys.argv) == 4:
    import pyperclip
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
        file_name = path.join(path.dirname(path.abspath(file)), f"{datetime.date.today()}.cryptic")

        with open(file_name, "wb") as file_encryption:
            file_encryption.write(EncryptedToken)  # Escribe el archivo encriptado

        print(Fore.CYAN + "Completado.")
        sleep(2)
        system("cls" if platform.system() == "Windows" else "clear")

    # Desencripta archivo
    elif sys.argv[1] == "-F" and sys.argv[2] == "-d" and sys.argv[3] != "":
        file = input("Archivo a desencriptar (usa la ruta completa si es necesario)\n> ")
        file_name = input("Nombre del nuevo archivo (incluye extension - No uses ruta completa)\n> ")
        # Agarra la ruta del archivo original para crear el nuevo archivo
        file_name = path.join(path.dirname(path.abspath(file)), f"{datetime.date.today()}.cryptic")
        # Agarra la contraseña y la convierte en bytes
        password = sys.argv[3].encode()
        sleep(1)
        print("Iniciando...")

        with open(file, "rb") as file_encrypted:
            token = file_encrypted.read()
            DecryptedToken = defs.decrypt(password, token)  # Desencripta el archivo

        with open(file_name, "wb") as final_file:  # Crea el archivo desencriptado
            final_file.write(DecryptedToken)  # Escribe el archivo desencriptado

        print(Fore.CYAN + "Completado.")
        sleep(2)
        system("cls" if platform.system() == "Windows" else "clear")

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
        system("cls" if platform.system() == "Windows" else "clear")

    elif sys.argv[1] == "-T" and sys.argv[2] == "-d" and sys.argv[3] != "":
        data = input("Que quieres desencriptar?\n> ").encode()
        password = sys.argv[3].encode()  # Agarra la contraseña y la convierte a bytes
        DecryptedToken = defs.decrypt(password, data)  # Desencripta el texto
        print(f"""
        Tu texto desencriptado es: {Fore.GREEN + DecryptedToken.decode()}
        {Fore.RESET + "Y ha sido copiado a tu portapapeles"}.""")  # Convierte los bytes a string para poder concatenarlos con Fore
        pyperclip.copy(DecryptedToken.decode())
        sleep(2)
        system("cls" if platform.system() == "Windows" else "clear")

# Error handle
else:
    print('''
    Puedes usar -F para usar el modo de archivos o usar -T para el modo de texto, luego:
    Puedes usar "-e" + tu contraseña para encriptar (paranoia.py -F -e password123)
    Puedes usar "-d" + tu contraseña para desencriptar (paranoia.py -T -d password123)
    Puedes usar "-h" para ver este mensaje
    Y puedes usar "-termux" para indicar que estas en termux!
''')
