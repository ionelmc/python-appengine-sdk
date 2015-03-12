#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

import io
import os
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import relpath
from os.path import splitext

from setuptools import find_packages
from setuptools import setup
import yaml


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='appengine-sdk',
    version=yaml.load(read(join('src', 'google_appengine', 'VERSION')))['release'],
    maintainer='Ionel Cristian Maries',
    maintainer_email='contact@ionelmc.ro',
    description='Un-official `pip install`-able AppEngine SDK.',
    long_description=read('README.rst'),
    keywords='google appengine gae sdk',
    url='https://github.com/ionelmc/python-appengine-sdk',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Installation/Setup',
    ],
    license='MIT',

    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,

    entry_points={
        'console_scripts': [
            'remote_api_shell = google_appengine.shim:remote_api_shell',
            'appcfg = google_appengine.shim:appcfg',
            'dev_appserver = google_appengine.shim:dev_appserver',
        ]
    },
)
