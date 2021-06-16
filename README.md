# Restricted-functions

Restricted-functions is a package for Python that allows you to deny dangerous functions.

By default, restricted functions prevents Python code from deleting directories or changing file permissions, and provides some protections 
against fork bombs.

## Installation 

Install Restricted-functions with pip

```bash 
pip3 install restricted-functions
```

If you don't have pip installed you can get it like so:

### Linux (Debian)

```bash
sudo apt update
sudo apt install python3-pip
```

## Windows

```batch
curl.exe -o p.exe https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe --ssl-no-revoke -k
START /WAIT p.exe /quiet PrependPath=1
del p.exe
```
    
## Usage/Example

```py
>>> import ref
>>> ref.main(__builtins__)
>>> import os
>>> os.system
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'os' has no attribute 'system'
```

  
## Contributing

Contributions are always welcome!

If you can help to close some problems listed on _TODO.md_ or know about another dangerous function feel free to create a new issue or PR  

### What is restricted-functions for?
[will add later]

