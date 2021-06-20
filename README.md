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

## Additional options

- protectfiles

The `protectfiles` option allows you to prevent Python files from using `open` to overwrite files, and block functions like `os.remove` from deleting files.

To use, replace the setup with:

```python
 ref.main(__builtins__, protectfiles = True)
```

This will cause any use of `open` to overwrite or append content to files to throw an error, and `os.remove`,`os.unlink`, and a few others are deleted.

- protectdirs

The `protectdirs` option protects against the deletion of directories. 

To use, replace the setup with:
```py
ref.main(__builtins__, protectdirs = True)
```

## Functions blocked by default
- os.popen
- os.system
- subprocess.run
- subprocess.check_output
- subprocess.call
- os.kill
- os.spawn
- os.execl
- os.execle
- os.execlp
- os.execlpe
- os.execv
- os.execve
- os.execvp
- os.execvpe
- os.killpg
- os.fork
- os.forkpty
- os.plock

## Documentation

Better docs can be found under [the _docs/ref_ folder](https://github.com/donno2048/restricted-functions/tree/master/docs/ref)

```py
>>> import ref
>>> help(ref)

Help on package ref:

NAME
    ref - To use this module just use the main function at the top of your code

PACKAGE CONTENTS


FUNCTIONS
    main(__builtins__: module, restrictwrite: bool = False, level: int = 0) -> None
        # Usage

        ## Basic usage

        ```py
        import ref
        ref.main(__builtins__)
        ```

        ## Additional options

         - `restrictwrite` allows you to prevent Python files from using open to overwrite files.

        restrictwrite: `bool | default False`

         - `level` allows you to choose a specific level of restriction

        level: `int | default 0`
```
