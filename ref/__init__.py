"""To use this module just use the main function at the top of your code"""
from types import ModuleType
import importlib
__level, __restrictwrite = None, None
def main(__builtins__: ModuleType, restrictwrite: bool = False, level: int = 0) -> None:
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
    global __level, __restrictwrite
    __level, __restrictwrite = level, restrictwrite
    __builtins__.__dict__['__import__'] = __import
    __builtins__.__dict__['open'] = __open
def __open(filename, mode="r", *args, **kwargs):
    global __restrictwrite
    if __restrictwrite and ("w" in mode or "a" in mode): raise AttributeError()
    return open(filename, mode, *args, **kwargs)
def __import(name, *args):
    global __level, __restrictwrite
    level, restrictwrite = __level, __restrictwrite
    try: M = importlib.__import__(name, *args)
    except AttributeError: return __import__
    if level >= 0:
        if name == 'os':
            try: del M.system
            except AttributeError: pass
            try: del M.rmdir
            except AttributeError: pass
            try: del M.unlink
            except AttributeError: pass
            try: del M.popen
            except AttributeError: pass
        elif name == 'subprocess':
            try: del M.run
            except AttributeError: pass
            try: del M.check_output
            except AttributeError: pass
            try: del M.call
            except AttributeError: pass
        elif name == 'shutil':
            try: del M.rmtree
            except AttributeError: pass
    if level >= 1:
        pass # todo: add here some other functions
    if restrictwrite:
        pass # todo: add here some other functions
    return M
