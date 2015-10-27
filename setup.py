# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='photonizer',
    version = '0.1.1',
    description='a command line tool to organize photos using plain files and folders.',
    author='Nico Di Rocco',
    author_email='dirocco.nico@gmail.com',
    url='http://nrocco.github.io',
    install_requires=[
        'PyExifTool==0.1'
    ],
    dependency_links = [
        'https://github.com/smarnach/pyexiftool/tarball/master#egg=pyexiftool-0.1',
    ],
    py_modules = [
        'photonizer'
    ],
    entry_points = {
        'console_scripts': [
            'photonizer = photonizer:main'
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

