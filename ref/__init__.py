"""To use this module just use the main function at the top of your code"""
from types import ModuleType
import importlib
__protectfiles, __silent = None, None
__restrict = {
    "os": ["system", "popen", "kill", "spawn", "execl", "execle", "execlp", "execlpe", "execv", "execve", "execvp", "execvpe", "killpg", "fork", "forkpty", "plock"],
    "subprocess": ["run", "check_output", "call"],
    "pathlib.Path": [],
    "shutil": []
}
def main(__builtins__: ModuleType, protectfiles: bool = False, protectdirs: bool = False, lockperms: bool = False, silent: bool = False) -> None:
    """
    # Usage

    ## Basic usage

    ```py
    import ref
    ref.main(__builtins__)
    ```
    
    ## Additional options
    
    - protectfiles
    
    The `protectfiles` option allows you to prevent Python files from using `open` to overwrite files, and block functions like `os.remove` from deleting files.
    
    To use, replace the setup with:
    
    ```py
    ref.main(__builtins__, protectfiles = True)
    ```
    
    This will cause any use of `open` to overwrite or append content to files to throw an error, and `os.remove`,`os.unlink`, and a few others are deleted.
    
    - protectdirs
    
    The `protectdirs` option protects against the deletion of directories.
    
    To use, replace the setup with:
    
    ```py
    ref.main(__builtins__, protectdirs = True)
    ```
    
    - lockperms
    
    This will prevent use of chmod in that Python file.
    
    To use, replace the setup with:
    
    ```py
    ref.main(__builtins__, lockperms = True)
    ```
    
    - silent
    
    This will replace any remove function with a dummy function.
    
    To use, replace the setup with:
    
    ```py
    ref.main(__builtins__, silent = True)
    ```
    
    That way, you won't get an error when trying to use `os.system("echo \"doing something that harms your system...\"")` but nothing will happen
    
    """
    global __protectfiles, __restrict, __silent
    __protectfiles, __silent = protectfiles, silent
    if protectfiles:
        __restrict["os"].extend(["remove", "unlink"])
        __restrict["pathlib.Path"].append("unlink")
    if protectdirs:
        __restrict["os"].extend(["rmdir", "removedirs"])
        __restrict["shutil"].append("rmtree")
        __restrict["pathlib.Path"].append("rmdir")
    if lockperms:
        __restrict["os"].append("chmod")
        __restrict["pathlib.Path"].append("chmod")
    __builtins__.__dict__['__import__'] = __import
    __builtins__.__dict__['open'] = __open
def __open(filename, mode="r", *args, **kwargs):
    global __protectfiles
    if __protectfiles and ("w" in mode or "a" in mode): raise AttributeError()
    return open(filename, mode, *args, **kwargs)
def __import(name, *args):
    global __restrict, __silent
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
