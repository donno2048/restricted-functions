from types import ModuleType
def main(__builtins__: ModuleType) -> None:
    import importlib
    def importer(name, *args):
        M = importlib.__import__(name, *args)
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
    __builtins__.__dict__['__import__'] = importer
