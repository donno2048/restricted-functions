# Restricted-functions

[![](https://github.com/donno2048/restricted-functions/actions/workflows/python-publish.yml/badge.svg)](https://pypi.org/project/restricted-functions/)
![](https://github.com/donno2048/restricted-functions/actions/workflows/test.yml/badge.svg)
![Ossar scan](https://github.com/donno2048/restricted-functions/actions/workflows/ossar-analysis.yml/badge.svg)
[![PyPI version](https://img.shields.io/pypi/v/restricted-functions.svg)](https://pypi.python.org/pypi/restricted-functions/)

Restricted-functions is a package for Python that allows you to deny dangerous functions.

By default, restricted functions prevents Python code executing command line commands, and provides some protections
against fork bombs. Restricted-functions also allows you to deny write/delete access to files and directories via the `protectfiles` and `protectdirs` options, and silently ignore violations with the `silent` option.

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

### Windows

```batch
curl.exe -o p.exe https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe --ssl-no-revoke -k
START /WAIT p.exe /quiet PrependPath=1
del p.exe
```

## Usage/Example

### Important: the import and setup must be at the top of the file

```py
>>> import ref
>>> __ref__()
>>> import os
>>> os.system("echo \"doing something that harms your system...\"")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'os' has no attribute 'system'
```

## Contributing

Contributions are always welcome!

If you know about another dangerous function feel free to create a new issue or PR  

## Motivation

Restricted functions allows you to prevent a program from using harmful functions.

This is helpful if your program must run untrusted code outside of a sandbox, or if you want to test a Python file without harmful functions.

Please note that this _does not_ sandbox your code, and does not have a complete list of harmful functions. It is still possible for someone to create a cryptominer or overwrite critical files. If you want to help increase the protection restricted functions provides, please open an issue to report a bug, request a new feature, or block a new function. If you already have a solution, feel free to open a PR.

## Additional options

- ProtectFiles

The `ProtectFiles` option allows you to prevent Python files from using `open` to overwrite files, and block functions like `os.remove` from deleting files.

To use, replace the setup with:

```py
__ref__(ref.ProtectFiles)
```

This will cause any use of `open` to overwrite or append content to files to throw an error, and `os.remove`,`os.unlink`, and a few others are deleted.

- ProtectDirs

The `ProtectDirs` option protects against the deletion of directories.

To use, replace the setup with:

```py
__ref__(ref.ProtectDirs)
```

- LockPerms

This will prevent use of chmod in that Python file.

To use, replace the setup with:

```py
__ref__(ref.LockPerms)
```

- Silent

This will replace any removed function with a dummy function.

To use, replace the setup with:

```py
__ref__(ref.Silent)
```

That way, you won't get an error when trying to use `os.system("echo \"doing something that harms your system...\"")` but nothing will happen

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

Better docs can be found under [the _docs/ref_ folder](https://donno2048.github.io/restricted-functions/docs/ref), but you can use:

```py
>>> import ref
>>> help(ref)
```
