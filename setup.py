#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

import io
import os
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext
from setuptools import find_packages
from setuptools import setup
from distutils.command.build import build
import yaml


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


class Build(build):
    def run(self):
        build.run(self)
        self.copy_file(
            join(dirname(__file__), 'src', 'appengine-sdk.pth'),
            join(self.build_lib, 'appengine-sdk.pth')
        )


setup(
    name='appengine-sdk',
    version='{}-{}'.format(
        yaml.load(read('src', 'appengine_sdk', 'google_appengine', 'VERSION'))['release'],
        read('src', 'appengine-sdk.build'),
    ),
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
            'remote_api_shell = appengine_sdk.commands:remote_api_shell',
            'appcfg = appengine_sdk.commands:appcfg',
            'dev_appserver = appengine_sdk.commands:dev_appserver',
        ]
    },
    cmdclass={
        'build': Build
    }
)
