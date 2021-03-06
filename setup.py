#!/usr/bin/env python3

import re
import sys

from setuptools import setup

if sys.version_info < (3, 3):
    print('ERROR: Buku requires at least Python 3.3 to run.')
    sys.exit(1)

with open('buku.py', encoding='utf-8') as f:
    version = re.search('__version__ = \'([^\']+)\'', f.read()).group(1)

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='buku',
    version=version,
    description='Powerful command-line bookmark manager. Your mini web!',
    long_description=long_description,
    author='Arun Prakash Jana',
    author_email='engineerarun@gmail.com',
    url='https://github.com/jarun/Buku',
    license='GPLv3',
    platforms=['any'],
    py_modules=['buku'],
    entry_points={
        'console_scripts': ['buku=buku:main']
    },
    extras_require={
        'HTTP': ['urllib3'],
        'CRYPTO': ['cryptography'],
        'HTML': ['beautifulsoup4'],
        'REQUESTS': ['requests']
    },
    test_suite='tests',
    tests_require=['pytest-cov', 'pytest-catchlog'],
    keywords='cli bookmarks tag utility',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Utilities'
    ]
)
