from setuptools import setup, find_packages
from setuptools.command.install import install
from ref import __version__
class Install(install):
    DATA = "\ntry: __import__('sys').modules['__main__'].__builtins__.__dict__['ref'] = __import__('ref')\nexcept ModuleNotFoundError: pass"
    def run(self):
        install.run(self)
        if self.DATA not in open(__import__('site').__file__, 'r').read().splitlines(): open(__import__('site').__file__, 'a').write("\n" + self.DATA)
setup(
    name='restricted-functions',
    version=__version__,
    license='MIT',
    author='Elisha Hollander, Alexander Bina',
    description="Restricted-functions is a package for Python that allows you to deny dangerous functions.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='http://restricted-functions.tk/',
    project_urls={
        'Documentation': 'https://github.com/donno2048/restricted-functions#readme',
        'Bug Reports': 'https://github.com/donno2048/restricted-functions/issues',
        'Source Code': 'https://github.com/donno2048/restricted-functions',
    },
    cmdclass={'install': Install},
    python_requires='>=3.0',
    packages=find_packages(),
    classifiers=['Programming Language :: Python :: 3']
)
