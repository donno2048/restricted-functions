from types import ModuleType
import importlib
def main(__builtins__: ModuleType) -> None:
    __builtins__.__dict__['__import__'] = importer
def importer(name, *args):
    try: M = importlib.__import__(name, *args)
    except AttributeError: pass
    else:
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
        return M
