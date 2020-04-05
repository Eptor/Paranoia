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

You can use:
```
pip install -r requirements.txt -y 
```
or
```
pip install -r requirements_linux.txt -y
```

or install the modules individually

Cryptogrphy module:

```
pip install cryptography
```

Colorama module:

```
pip install colorama
```

Pyperclip module (only windows for now):

```
pip install pyperclip
```

And for the GUI you will need the PySimpleGui module:

```
pip install PySimpleGUI
```

Repo:

You can clone or download this repository

## Use

* You can use **-F** *(paranoia.py -F -e password123)* to use the Files mode
* You can use **-T** *(paranoia.py -T -d password123)* for Text mode, then:
* You can use **"-e"** + your password to enctypt *(paranoia.py -F -e password123)*
* You can use **"-d"** + your password to decrypt *(paranoia.py -T -d password123)*
* You can use **"-h"** to show this message in your terminal *(paranoia.py -h)*
* And you can use **-termux** to indicate you are on termux! 

## Termux

Compatibility with termux (and linux in general) seems finished.

## Graphic User Interface

The GUI was added for better and faster user interaction, only the files mode is enabled on the GUI.

GUI icons by <a href="https://iconscout.com/contributors/nixxdsgn">NIXX Design</a> on <a href="https://iconscout.com">Iconscout</a>