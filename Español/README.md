# Paranoia

Un encriptador para texto y archivos (de momento solo archivos) escritos en python 3 usando el modulo de criptografía

## Salt
Puedes cambiar el salt usado en las funciones, solo usa el modulo os:
```
os.urandom(16)
```
and change the salt value on Defs/crypto_defs.py

## Instalación

Cryptogrphy:

```sh
pip install cryptography
```

Repo:

You can clone or download this repository
