from types import ModuleType
def main(__builtins__: ModuleType) -> None:
    import importlib
    def importer(name, *args):
        M = importlib.__import__(name, *args)
        if name == 'os':
            function = None
            try: function = M.system
            except AttributeError: pass
            else: del M.system
            try: function = M.rmdir
            except AttributeError: pass
            else: del M.rmdir
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
