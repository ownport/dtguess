
try:
    from setuptools import setup, find_packages
except ImportError, err:
    raise ImportError('Cannot import setup() and find_packages(), %s' % err)

from dtguess import __title__
from dtguess import __version__

setup(
    name=__title__,
    version=__version__,
    description='Python library for data type guessing',
    author="Andrey Usov",
    author_email="ownport@gmail.com",
    url='https://github.com/ownport/dtguess',
    py_modules=['dtguess'],
    packages=find_packages(),
    install_requires=[
        'six',
        'python-dateutil',
    ]
)
