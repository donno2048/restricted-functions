__ref__(*range(4))
from sys import version, platform, exit, argv, stdin
from argparse import ArgumentParser, FileType
from code import InteractiveConsole
def main():
    parser = ArgumentParser(usage = argv[0] + ' [option] ... [-c cmd | -m mod | file | -] [arg] ...')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', metavar='cmd', dest='cmd', type=str, help='program passed in as string (terminates option list)')
    group.add_argument('-m', metavar='mod', dest='mod', type=str, help='run library module as a script (terminates option list)')
    group.add_argument('file', nargs='?', type=FileType('r'), help='program read from script file')
    group.add_argument('-', dest='raw', action='store_true', help='program read from stdin (default; interactive mode if a tty)')
    parser.add_argument('-E', dest='environment', action='store_true', help='ignore PYTHON* environment variables (such as PYTHONPATH)')
    parser.add_argument('-s', dest='site', action='store_true', help='don\'t add user site directory to sys.path; also PYTHONNOUSERSITE')
    parser.add_argument('-I', dest='isolate', action='store_true', help='isolate Python from the user\'s environment (implies -E and -s)')
    parser.add_argument('-x', dest='skip', action='store_true', help='skip first line of source, allowing use of non-Unix forms of #!cmd')
    parser.add_argument('-q', dest='quiet', action='store_false', help='don\'t print version and copyright messages on interactive startup')
    parser.add_argument('-V', dest='version', action='store_true', help='print the Python version number and exit (also --version)')
    parser.add_argument('arg', nargs='*', type=str)
    args = parser.parse_args()
    if args.version:
        exit("Python %s" % version.split(' ')[0])
    if args.arg:
        import sys
        sys.argv = args.arg
    if args.isolate:
        args.environment = True
        args.site = False
    if args.site:
        import sys, site
        for dir in site.getsitepackages():
            if dir in sys.path:
                sys.path.remove(dir)
        site_packages = []
        for i in sys.path:
            if "site-packages" in i: # ugly solution
                site_packages += [i]
        for package_path in site_packages:
            sys.path.remove(package_path)
    if args.environment:
        import os, re
        pattern, mathces = re.compile("PYTHON*"), []
        for i in os.environ:
            if re.match(pattern, i):
                mathces += [i]
        for match in mathces:
            del os.environ[match]
    if args.raw:
        exit(exec(stdin.read()))
    if args.cmd:
        exit(exec(args.cmd))
    if args.mod:
        __import__(args.mod)
        exit()
    if args.file:
        exit(exec("".join(args.file.readlines()[args.skip:])))
    if args.quiet:
        print("Python %s on %s\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information." % (version, platform))
    inter, flag = InteractiveConsole(), False
    while True:
        try: flag = inter.push(input(">>> " if not flag else "... "))
        except KeyboardInterrupt: print("\nKeyboardInterrupt")
        except EOFError: break
if __name__ == '__main__': main()
