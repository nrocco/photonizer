#!/usr/bin/env python
import re
import io
import codecs

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class NoseTestCommand(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # Run nose ensuring that argv simulates running nosetests directly
        import nose
        nose.run_exit(argv=['nosetests'])


setup(
    name = 'photonizer',
    description = 'a command line tool to organize photos using plain files and folders.',
    version = re.search(r'''^__version__\s*=\s*["'](.*)["']''', open('photonizer/__init__.py').read(), re.M).group(1),
    author = 'Nico Di Rocco',
    author_email = 'dirocco.nico@gmail.com',
    url = 'https://github.com/nrocco/photonizer',
    license = 'GPLv3',
    long_description = codecs.open('README.rst', 'rb', 'utf-8').read(),
    test_suite = 'nose.collector',
    download_url = 'https://github.com/nrocco/photonizer/tags',
    include_package_data = True,
    install_requires = [
        'pycli-tools',
        'bottle',
        'Pillow',
        'pyexiftool',
    ],
    dependency_links = [
        'https://github.com/smarnach/pyexiftool/archive/v0.2.0.tar.gz#egg=pyexiftool-0.2.0',
    ],
    tests_require = [
        'nose',
        'coverage',
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
    ],
    cmdclass = {
        'test': NoseTestCommand
    }
)
