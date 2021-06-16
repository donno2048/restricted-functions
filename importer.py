try:
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
        return M
    __builtins__.__dict__['__import__'] = importer
except Exception as err:
    with open("output.txt",'w') as f:
        f.write("Error: {}".format(err))
        f.close()
else:
    with open("output.txt","w") as f:
        f.write("No errors")
        f.close()
