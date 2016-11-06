from setuptools import setup

from dtguess import __title__
from dtguess import __version__

setup(
    name=__title__,
    version=__version__,
    py_modules=['dtguess'],
    install_requires=[
        'python-dateutil', 'six'
    ]
)
