from types import ModuleType
import importlib
level_, restrictwrite_ = None, None
def main(__builtins__: ModuleType, restrictwrite: bool = False, level: int = 0) -> None:
    global level_, restrictwrite_
    level_, restrictwrite_ = level, restrictwrite
    __builtins__.__dict__['__import__'] = import_
    __builtins__.__dict__['open'] = open_
def open_(filename, mode="r", *args, **kwargs):
    global restrictwrite_
    if restrictwrite_ and ("w" in mode or "a" in mode): raise AttributeError()
    return open(filename, mode, *args, **kwargs)
def import_(name, *args):
    global level_, restrictwrite_
    level, restrictwrite = level_, restrictwrite_
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
