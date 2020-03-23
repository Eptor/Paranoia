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
        file = Path(input("Archivo (usa toda la ruta si es necesario)\n> ")) # Transforma el nombre del archivo a ruta de windows
        password = sys.argv[2].encode() # Agarra la contraseña y la convierte a bytes
        sleep(1)
        print("Iniciando...")
        EncryptedToken = defs.encrypt(password, file)
        with open("encrypted.file", "wb") as file_encryption:
            file_encryption.write(EncryptedToken)
            file_encryption.close()
        print("Proceso completado.")
        system("cls")
    # Decrypt
    elif sys.argv[1] == "-d" and sys.argv[2] != "":
        file = input("Archivo (usa toda la ruta si es necesario)\n> ")
        file_name = input("Nombre del nuevo archivo (Incluya extension)\n>") # Guarda el nombre final del archivo
        password = sys.argv[2].encode() # Agarra la contraseña y la convierte a bytes
        sleep(1)
        print("Iniciando...")
        with open(file, "r") as file_encrypted:
            token = file_encrypted.read().encode() # Lee el archivo y convierte el string a bytes
            DecryptedToken = defs.decrypt(password, token) # Desencripta el texto
            file_encrypted.close()
        with open(file_name, "wb") as final_file: # Crea el archivo desencritado
            final_file.write(DecryptedToken)
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
