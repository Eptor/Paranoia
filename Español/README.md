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

Puedes usar:
```
pip install -r requirements.txt -y // pip install -r requirements_linux.txt -y
```

o instalar los modulos individualmente

Modulo cryptogrphy:

```
pip install cryptography
```

Modulo Colorama:

```
pip install colorama
```

Modulo pyperclip (solo windows de momento):

```
pip install pyperclip
```

Y para la interfaz grafica necesitas el modulo PySimpleGui:

```
pip install PySimpleGUI
```

Repo:

Puedes descargar o clonar este repositorio

## Uso

* Puedes usar **-F** *(paranoia.py -F -e password123)* para usar el modo de archivos
* Puedes usar **-T** *(paranoia.py -T -d password123)* para el modo de texto , luego:
* Puedes usar **"-e"** + tu contraseña para encriptar *(paranoia.py -e password123)*
* Puedes usar **"-d"** + tu contraseña para desencriptar *(paranoia.py -d password123)*
* Puedes usar **"-h"** para ver este mensaje en tu terminal *(paranoia.py -h)*
* Y puedes usar **-termux** para indicar que estas en termux!

## Termux

La compatibilidad con termux (y linux en general) para finalizada.

## Interfaz Grafica de Usuario

La interfaz se añadio para una mejor y mas rapida interaccion del usuaio, solo el modo de archivos está habilitado en la interfaz.
Puedes encontrarlo <a href="https://github.com/Eptor/Paranoia_GUI">aqui</a>

Iconos de la interfaz por <a href="https://iconscout.com/contributors/nixxdsgn">NIXX Design</a> en <a href="https://iconscout.com">Iconscout</a>