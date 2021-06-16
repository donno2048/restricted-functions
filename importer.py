def remove_if_not_already_removed(*functions):
    for function in functions:
        try: del function
        except AttributeError: pass
try:
    import importlib
    def importer(name, *args):
        M = importlib.__import__(name, *args)
        if name == 'os':
            try: del M.system # for some reason won't work inside the function
            except AttributeError: pass
            remove_if_not_already_removed(M.rmdir)
        elif name == 'subprocess':
            remove_if_not_already_removed(M.run, M.check_output, M.call)
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
