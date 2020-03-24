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
        file = Path(input("Archivo a encriptar (usa toda la ruta si es necesario)\n> "))  # Transforma el nombre del archivo a ruta de windows
        password = sys.argv[2].encode()  # Agarra la contraseña y la convierte a bytes
        sleep(1)
        print("Iniciando...")
        EncryptedToken = defs.encrypt(password, file)
        file_name = path.dirname(path.abspath(file)) + "\encrypted.file"  # Toma la ruta del archivo original y la usa para crear el archivo encriptado

        with open(file_name, "wb") as file_encryption:
            file_encryption.write(EncryptedToken)  # Escribe lo encriptado en el archivo
            file_encryption.close()

        print("Proceso completado.")
        system("cls")

    # Decrypt
    elif sys.argv[1] == "-d" and sys.argv[2] != "":
        file = input("Archivo a desencriptar (usa toda la ruta si es necesario)\n> ")
        file_name = input("Nombre del nuevo archivo (Incluya extension - No use ruta completa)\n>")  # Guarda el nombre final del archivo
        file_name = f"{path.dirname(path.abspath(file))}\{file_name}"  # Toma la ruta del archivo original y la usa para crear el archivo desencriptado     
        password = sys.argv[2].encode()  # Agarra la contraseña y la convierte a bytes
        sleep(1)
        print("Iniciando...")

        with open(file, "r") as file_encrypted:
            token = file_encrypted.read().encode()  # Lee el archivo y convierte el string a bytes
            DecryptedToken = defs.decrypt(password, token)  # Desencripta el texto
            file_encrypted.close()

        with open(file_name, "wb") as final_file:  # Crea el archivo desencritado
            final_file.write(DecryptedToken)  # Escribe el archivo desencriptado
            final_file.close()

        print("Proceso completado.")
        system("cls")

# Manejo de errores
elif len(sys.argv) == 2 and sys.argv[1] == "-h" or len(sys.argv) < 2:
    print('''
    Puedes usar "-e" + tu contraseña para encreiptar (paranoia.py -e password123)
    Puedes usar "-d" + tu contraseña para desencriptar (paranoia.py -d password123)
    Puedes usar "-h" para mostrar este mensaje
''')
elif len(sys.argv) > 3:
    print("Usaste mas de 2 parametros")
