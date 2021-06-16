try:
    import importlib
    def importer(name, *args):
        M = importlib.__import__(name, *args)
        if name == 'os':
            del M.system
        elif name == 'subprocess':
            del M.run
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
