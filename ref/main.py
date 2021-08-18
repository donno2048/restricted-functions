try: import __init__
except ModuleNotFoundError: pass
else:
    __ref__(*range(4))
    from sys import version, platform
    from code import InteractiveConsole
    def main():
        print("Python %s on %s\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information." % (version, platform))
        inter, flag = InteractiveConsole(), False
        while True:
            try: flag = inter.push(input(">>> " if not flag else "... "))
            except KeyboardInterrupt: print("\nKeyboardInterrupt")
            except EOFError: break
    if __name__ == '__main__': main()
