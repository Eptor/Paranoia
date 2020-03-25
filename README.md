[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/ArcticBabe/Paranoia/?ref=repository-badge)
# Paranoia

An encryptor for text and files, written in python 3 using the cryptography module

## Salt
You can change the salt used by the functions, just use the os module:
```
os.urandom(16)
```
and change the salt value on Defs/crypto_defs.py

## Install

Cryptogrphy:

```
pip install cryptography
```

Repo:

You can clone or download this repository

## Use

* You can use **-F** *(paranoia.py -F -e password123)* to use the Files mode
* You can use **-T** *(paranoia.py -T -d password123)* for Text mode, then:
* You can use **"-e"** + your password to enctypt *(paranoia.py -F -e password123)*
* You can use **"-d"** + your password to decrypt *(paranoia.py -T -d password123)*
* You can use **"-h"** to show this message in your terminal *(paranoia.py -h)*

## Termux

termux compatibility is a work in progress at the moment