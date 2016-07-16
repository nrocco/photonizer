# -*- coding: utf-8 -*-
import re
from setuptools import setup, find_packages

setup(
    name='photonizer',
    version = re.search(r'''^__version__\s*=\s*["'](.*)["']''', open('photonizer/__init__.py').read(), re.M).group(1),
    description='a command line tool to organize photos using plain files and folders.',
    author='Nico Di Rocco',
    author_email='dirocco.nico@gmail.com',
    url='http://nrocco.github.io',
    install_requires=[
        'pycli-tools>=2.0.2',
        'PyExifTool==0.1',
        'Pillow==3.3.0',
    ],
    dependency_links = [
        'https://github.com/smarnach/pyexiftool/tarball/master#egg=pyexiftool-0.1',
    ],
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'photonizer = photonizer.__main__:main'
        ]
    },
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities'
    ],
)
