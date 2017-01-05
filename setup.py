# -*- coding: utf-8 -*-
#!/usr/bin/env python
import re
import io
import codecs

from setuptools import setup, find_packages
def load_requirements(filename):
    with io.open(filename, encoding='utf-8') as reqfile:
        return [line.strip() for line in reqfile if not line.startswith('#')]


setup(
    name = 'photonizer',
    description = 'a command line tool to organize photos using plain files and folders.',
    version = re.search(r'''^__version__\s*=\s*["'](.*)["']''', open('photonizer/__init__.py').read(), re.M).group(1),
    author = 'Nico Di Rocco',
    author_email = 'dirocco.nico@gmail.com',
    url = 'http://nrocco.github.io',
    license = 'GPLv3',
    install_requires = [
        'pycli-tools>=2.0.2',
        'bottle==0.12.11',
        'Pillow==4.0.0',
        'pyexiftool',
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
    ],
)
