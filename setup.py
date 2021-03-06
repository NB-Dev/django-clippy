import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name = "django-clippy",
    version = "0.0.2",
    author = "Igor Guerrero",
    author_email = "igfgt1@gmail.com",
    description = ("A copy to clipboard widget for Django."),
    license = "MIT",
    keywords = "django clippy clipboard",
    url = "https://github.com/NB-Dev/django-clippy",
    include_package_data = True,
    packages=find_packages(exclude=('example',)),
    exclude=['*.tests', 'example'],
    install_requires=['Django >=1.7',],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.6",
        "License :: OSI Approved :: MIT License",
    ],
)
