"""To use this module just use the main function at the top of your code."""

from sys import modules as __modules
import importlib
_ProtectFiles, _ProtectDirs, _LockPerms, _Silent = range(4)
__version__, __file__, __protectfiles, __silent, __oldopen = "1.3.1", None, None, None, open
__restrict = {
    "os": ["system", "popen", "kill", "spawn", "execl", "execle", "execlp", "execlpe", "execv", "execve", "execvp", "execvpe", "killpg", "fork", "forkpty", "plock", "popen2", "popen3"],
    "subprocess": ["run", "check_output", "call", "Popen", "check_call", "getstatusoutput", "getoutput"],
    "pathlib.Path": [],
    "shutil": []
}
def ref(*args) -> None:
    """
    # Usage

    ## Basic usage

    ```py
    __ref__() # no need to import anything
    ```

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

    """
    global __protectfiles, __restrict, __silent
    protectfiles, protectdirs, lockperms, silent = map(lambda x: x in args, range(4))
    __protectfiles, __silent = protectfiles, silent
    if protectfiles:
        __restrict["os"].extend(["remove", "unlink", "rename", "replace"])
        __restrict["pathlib.Path"].append("unlink")
        __restrict["shutil"].append("move")
    if protectdirs:
        __restrict["os"].extend(["rmdir", "removedirs", "rename", "replace"])
        __restrict["shutil"].extend(["rmtree", "move"])
        __restrict["pathlib.Path"].append("rmdir")
    if lockperms:
        __restrict["os"].append("chmod")
        __restrict["pathlib.Path"].append("chmod")
    __modules['__main__'].__builtins__.__dict__['__import__'] = __import
    __modules['__main__'].__builtins__.__dict__['open'] = __open
def __open(filename, mode="r", *args, **kwargs):
    if __protectfiles and ("w" in mode or "a" in mode): raise AttributeError()
    return __oldopen(filename, mode, *args, **kwargs)
def __import(name, *args):
    try: M = importlib.__import__(name, *args)
    except AttributeError: return __import__
    for mod in __restrict:
        if name == mod:
            for method in __restrict[mod]:
                try:
                    if __silent: M.__dict__[method] = lambda *_:None
                    else: del M.__dict__[method]
                except (AttributeError, KeyError): pass
    return M
if __name__ != '__main__': __modules['__main__'].__builtins__.__dict__['__ref__'] = ref
