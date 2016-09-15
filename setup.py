#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('history.rst') as history_file:
    history = history_file.read()

requirements = [
    #TODO: put package requirements here
    'setuptools==25.2.0',
    'wheel==0.29.0',
    'pip==8.1.2',
]


setup(
    name='talalprotocol',
    version='0.1.0',
    packages=['talalprotocol'],
    url='https://github.com/s3nu/talalprotocol',
    license='',
    author='Team ThugThug',
    author_email='talalkhalil206@gmail.com',
    description='Deep Layered Encryption',
    package_dir={'talalprotocol':
                     'talalprotocol'},
    keywords='talalprotocol',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Internal Testing',
        'Natural Language :: English',
        'License:: Licensed Material - Property of Team Standy. Proprietary License',
        'Python Package :: Encryption Package for Robust Security Use'
        'Operating System :: MacOS',
        "Programming Language :: Python :: 2.7 :: Testing in Progress",
        'Programming Language :: Python :: 2.6 :: Testing In Progress',
        'Programming Language :: Python :: 3   :: Works',
        'Programming Language :: Python :: 3.3 :: Works',
        'Programming Language :: Python :: 3.4 :: Works',
        'Programming Language :: Python :: 3.5 :: Works',
    ],
)
