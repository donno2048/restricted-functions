from setuptools import setup, find_packages
setup(
    name='restricted-functions',
    version='1.1.2',
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
    python_requires='>=3.0',
    packages=find_packages(),
    classifiers=['Programming Language :: Python :: 3']
)
