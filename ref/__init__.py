"""To use this module just use the main function at the top of your code"""
from types import ModuleType
import importlib
__protectfiles, __protectdirs, __lockperms = None, None, None
def main(__builtins__: ModuleType, protectfiles: bool = False, protectdirs: bool = False, lockperms: bool = False) -> None:
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
    ref.main(__builtins__,lockperms = True)
    ```
    
    """
    global __protectfiles, __protectdirs, __lockperms
    __protectfiles, __protectdirs, __lockperms = protectfiles, protectdirs, lockperms
    __builtins__.__dict__['__import__'] = __import
    __builtins__.__dict__['open'] = __open
def __open(filename, mode="r", *args, **kwargs):
    global __protectfiles
    if __protectfiles and ("w" in mode or "a" in mode): raise AttributeError()
    return open(filename, mode, *args, **kwargs)
def __import(name, *args):
    global __protectfiles, __protectdirs
    protectfiles, protectdirs, lockperms = __protectfiles, __protectdirs, __lockperms
    try: M = importlib.__import__(name, *args)
    except AttributeError: return __import__
    if name == 'os':
        #if it is the os module being imported
        try: del M.system
        except AttributeError: pass
        try: del M.popen
        except AttributeError: pass
        try: del M.kill
        except AttributeError: pass
        try: del M.spawn
        except AttributeError: pass
        try: del M.execl
        except AttributeError: pass
        try: del M.execle
        except AttributeError: pass
        try: del M.execlp
        except AttributeError: pass
        try: del M.execlpe
        except AttributeError: pass
        try: del M.execv
        except AttributeError: pass
        try: del M.execve
        except AttributeError: pass
        try: del M.execvp
        except AttributeError: pass
        try: del M.execvpe
        except AttributeError: pass
        try: del M.killpg
        except AttributeError: pass
        try: del M.fork
        except AttributeError: pass
        try: del M.forkpty
        except AttributeError: pass
        try: del M.plock
        except AttributeError: pass
    elif name == 'subprocess':
        try: del M.run
        except AttributeError: pass
        try: del M.check_output
        except AttributeError: pass
        try: del M.call
        except AttributeError: pass
    if protectfiles:
        "prevent files from being deleted"
        if name == 'os':
            try: del M.remove
            except AttributeError: pass
            try: del M.unlink
            except AttributeError: pass
        elif name == 'pathlib.Path':
            try: del M.unlink
            except AttributeError: pass
    if protectdirs:
        "prevent dirs from being deleted"
        if name == 'os':
            try: del M.rmdir
            except AttributeError: pass
            try: del M.removedirs
            except AttributeError: pass
        elif name == 'shutil':
            try: del M.rmtree
            except AttributeError: pass
        elif name == 'pathlib.Path':
            try: del M.rmdir
            except AttributeError: pass
    if lockperms:
        "Prevent chmod from being used"
        if name == 'os':
            try: del M.chmod
            except AttributeError: pass
        elif name == 'pathlib.Path':
            try: del M.chmod
            except AttributeError: pass
    return M
