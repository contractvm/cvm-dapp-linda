#!/usr/bin/python3
# Copyright (c) 2016 Davide Gessa, Sebastian Podda
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from setuptools import find_packages
from setuptools import setup

setup(name='linda',
	version='0.1',
	description='Linda dapp library',
	author='Davide Gessa, Sebastian Podda',
	setup_requires='setuptools',
	author_email='gessadavide@gmail.com, none@none',
	package_dir={'':'library'},
	packages=['linda']
)
