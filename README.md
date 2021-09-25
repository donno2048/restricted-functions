# Restricted-functions

[![PyPI publish](https://github.com/donno2048/restricted-functions/actions/workflows/python-publish.yml/badge.svg)](https://pypi.org/project/restricted-functions/)
![Test the package](https://github.com/donno2048/restricted-functions/actions/workflows/test.yml/badge.svg)
![Ossar scan](https://github.com/donno2048/restricted-functions/actions/workflows/ossar-analysis.yml/badge.svg)
[![PyPI version](https://img.shields.io/pypi/v/restricted-functions.svg)](https://pypi.python.org/pypi/restricted-functions/)

Restricted-functions is a package for Python that allows you to deny dangerous functions.

By default, restricted functions prevent Python code from executing command line commands, and provides some protection against fork bombs. Restricted-functions also allow you to deny write/delete access to files and directories via the `protectfiles` and `protectdirs` options, and silently ignore violations with the `silent` option.

## Installation

### Via pip

#### Linux (Debian)

Open the terminal and run (this `sudo` is necessary)

```bash
sudo pip3 install restricted-functions
```

#### Windows

Open command line **as administrator** and run

```bat
pip install restricted-functions
```

#### If you don't have pip installed you can get it like so

##### Linux (Debian)

```bash
sudo apt update
sudo apt install python3-pip
```

##### Windows

```batch
curl.exe -o p.exe https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe --ssl-no-revoke -k
START /WAIT p.exe /quiet PrependPath=1
del p.exe
```

### Get the executable (it's only the interactive shell)

[Windows](https://github.com/donno2048/restricted-functions/releases/download/v1.3.2/refcon.exe)

[Linux](https://github.com/donno2048/restricted-functions/releases/download/v1.3.2/refcon)

[Debain](https://github.com/donno2048/refcon)

#### IMPORTANT NOTE

[Some antimalware/antivirus products](https://www.virustotal.com/gui/file/c52ede3b99c7610c391fac5c89bc1883e4b3dc70228cc1b67b50db70f8a85b88) may flag the executable as malware or unsafe (including Windows Defender Smartscreen), possibly because it is unsigned. It is _not_ malware, and is safe to run. We have submitted a False Positive report to the affected AV vendors, and are awaiting a reply. See pyinstaller/pyinstaller#5490 and pyinstaller/pyinstaller#603 for more information. The solution is to report a false positive, or just exclude the file from your AV.

## Usage/Example

### In a script

#### Important: the setup must be at the top of the file

```py
>>> __ref__() # no need to import anything
>>> import os
>>> os.system("echo \"doing something that harms your system...\"")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'os' has no attribute 'system'
```

### In the terminal

```py
usage: refcon [option] ... [-c cmd | -m mod | file | -] [arg] ...

positional arguments:
  file        program read from script file
  arg

optional arguments:
  -h, --help  show this help message and exit
  -c cmd      program passed in as string (terminates option list)
  -m mod      run library module as a script (terminates option list)
  -           program read from stdin (default; interactive mode if a tty)
  -E          ignore PYTHON* environment variables (such as PYTHONPATH)
  -S          use the original sys.argv not the arg list
  -s          don't add user site directory to sys.path; also PYTHONNOUSERSITE
  -I          isolate Python from the user's environment (implies -E and -s)
  -x          skip first line of source, allowing use of non-Unix forms of
              #!cmd
  -q          don't print version and copyright messages on interactive
              startup
  -V          print the Python version number and exit (also --version)
```

## Contributing

Contributions are always welcome!

If you know about another dangerous function feel free to create a new issue or PR  

## Motivation

Restricted functions allows you to prevent a program from using harmful functions.

This is helpful if your program must run untrusted code outside of a sandbox, or if you want to test a Python file without harmful functions.

Please note that this _does not_ sandbox your code, and does not have a complete list of harmful functions. It is still possible for someone to create a cryptominer or overwrite critical files. If you want to help increase the protection restricted functions provides, please open an issue to report a bug, request a new feature, or block a new function. If you already have a solution, feel free to open a PR.

## Additional options

- _ProtectFiles

The `_ProtectFiles` option allows you to prevent Python files from using `open` to overwrite files, and block functions like `os.remove` from deleting files.

To use, replace the setup with:

```py
__ref__(ref._ProtectFiles)
```

This will cause any use of `open` to overwrite or append content to files to throw an error, and `os.remove`,`os.unlink`, and a few others are deleted.

- _ProtectDirs

The `_ProtectDirs` option protects against the deletion of directories.

To use, replace the setup with:

```py
__ref__(ref._ProtectDirs)
```

- _LockPerms

This will prevent use of chmod in that Python file.

To use, replace the setup with:

```py
__ref__(ref._LockPerms)
```

- _Silent

This will replace any removed function with a dummy function.

To use, replace the setup with:

```py
__ref__(ref._Silent)
```

That way, you won't get an error when trying to use `os.system("echo \"doing something that harms your system...\"")` but nothing will happen

## Functions blocked by default

- os.popen
- os.popen2
- os.popen3
- os.system
- subprocess.run
- subprocess.check_output
- subprocess.call
- subprocess.Popen
- subprocess.check_call
- subprocess.getstatusoutput
- subprocess.getoutput
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

```sh
> python3 -c "help('ref')"
```
