from types import ModuleType
import importlib
def main(__builtins__: ModuleType) -> None:
    __builtins__.__dict__['__import__'] = importer
def importer(name, *args, level: int = 0):
    try: M = importlib.__import__(name, *args)
    except AttributeError: return __import__
    if level >= 0:
        if name == 'os':
            try: del M.system
            except AttributeError: pass
            try: del M.rmdir
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
    return M
