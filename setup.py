#!/usr/bin/env python
import re
import io
import codecs

from setuptools import setup, find_packages


setup(
    name = 'photonizer',
    description = 'a command line tool to organize photos using plain files and folders.',
    version = '0.5.2',
    author = 'Nico Di Rocco',
    author_email = 'dirocco.nico@gmail.com',
    url = 'https://github.com/nrocco/photonizer',
    license = 'GPLv3',
    long_description = codecs.open('README.rst', 'rb', 'utf-8').read(),
    download_url = 'https://github.com/nrocco/photonizer',
    include_package_data = True,
    install_requires = [
        'pycli-tools==2.0.2',
        'bottle==0.12.12',
        'Pillow==4.0.0',
        'pyexiftool==0.1',
    ],
    dependency_links = [
        'https://github.com/smarnach/pyexiftool/archive/v0.2.0.tar.gz#egg=pyexiftool-0.2.0',
    ],
    entry_points = {
        'console_scripts': [
            'photonizer = photonizer.__main__:main'
        ]
    },
    packages = find_packages(),
    zip_safe = False,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities'
    ]
)
