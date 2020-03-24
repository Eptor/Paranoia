[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/ArcticBabe/Paranoia/?ref=repository-badge)
# Paranoia

Un encriptador para texto y archivos, escrito en python 3 usando el modulo de criptografía

## Salt

Puedes cambiar el salt usado en las funciones, solo usa el modulo os:
```
os.urandom(16)
```
y cambia el valor de salt en Defs/crypto_defs.py

## Instalación

Modulo cryptogrphy:

```
pip install cryptography
```

Repo:

Puedes descargar o clonar este repositorio

## Uso

* Puedes usar **-F** *(paranoia.py -F -e password123)* para usar el modo de archivos
* Puedes usar **-T** *(paranoia.py -T -d password123)* para el modo de texto , luego:
* Puedes usar **"-e"** + tu contraseña para encriptar *(paranoia.py -e password123)*
* Puedes usar **"-d"** + tu contraseña para desencriptar *(paranoia.py -d password123)*
* Puedes usar **"-h"** para ver este mensaje en tu terminal *(paranoia.py -h)*