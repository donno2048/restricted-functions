from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
from ref import __version__
def write():
    DATA = "\ntry: __import__('sys').modules['__main__'].__builtins__.__dict__['ref'] = __import__('ref')\nexcept ModuleNotFoundError: pass"
    if DATA not in open(__import__('site').__file__, 'r').read(): open(__import__('site').__file__, 'a').write(DATA)
class Install(install):
    def run(self):
        install.run(self)
        write()
class Develop(develop):
    def run(self):
        develop.run(self)
        write()
class EggInfo(egg_info):
    def run(self):
        egg_info.run(self)
        write()
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
    cmdclass={
        'install': Install,
        'develop': Develop,
        'egg_info': EggInfo
    },
    python_requires='>=3.0',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 6 - Mature',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Security'
    ],
    zip_safe=False,
    entry_points={ 'console_scripts': [ 'refcon=ref.__main__:main' ] }
)
