"""To use this module just use the main function at the top of your code"""
from types import ModuleType
import importlib
__level, __protectfiles, __protectdirs = None, None, None
def main(__builtins__: ModuleType, protectfiles: bool = False, protectdirs: bool = False, level: int = 0) -> None:
    """
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
    """
    global __level, __protectfiles, __protectdirs
    __level, __protectfiles, __protectdirs = level, protectfiles, protectdirs
    __builtins__.__dict__['__import__'] = __import
    __builtins__.__dict__['open'] = __open
def __open(filename, mode="r", *args, **kwargs):
    global __protectfiles
    if __protectfiles and ("w" in mode or "a" in mode): raise AttributeError()
    return open(filename, mode, *args, **kwargs)
def __import(name, *args):
    global __level, __protectfiles, __protectdirs
    level, protectfiles, protectdirs = __level, __protectfiles, __protectdirs
    try: M = importlib.__import__(name, *args)
    except AttributeError: return __import__
    if level >= 0:
        if name == 'os':
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
        if name == 'os':
            try: del M.remove
            except AttributeError: pass
            try: del M.unlink
            except AttributeError: pass
        elif name == 'pathlib.Path':
            try: del M.unlink
            except AttributeError: pass
    if protectdirs:
        if name == 'os':
            try: del M.unlink
            except AttributeError: pass
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
            try: del M.unlink
            except AttributeError: pass
    return M
