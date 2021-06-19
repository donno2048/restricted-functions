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
>>> os.system("echo \"doing something that harms your system...\"")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'os' has no attribute 'system'
```

  
## Contributing

Contributions are always welcome!

If you can help to close some problems listed on _TODO.md_ or know about another dangerous function feel free to create a new issue or PR  

## Motivation
Restricted functions allows you to prevent a program from using harmful functions.

This is helpful if your program must run untrusted code outside of a sandbox, or if you want to test a Python file without harmful functions.

Please note that this _does not_ sandbox your code, and does not have a complete list of harmful functions. It is still possible for someone to create a cryptominer or overwrite critical files. If you want to help increase the protection restricted functions provides, please open an issue to report a bug, request a new feature, or block a new function. If you already have a solution, feel free to open a PR.

### Additional options
- restrictwrite
The <code>restrictwrite</code> option allows you to prevent Python files from using `open` to overwrite files.<br>
To use, replace the setup with:
```python
 ref.main(__builtins__, restrictwrite = True)
```
This will cause any use of `open` to overwrite or append content to files to throw an error.

