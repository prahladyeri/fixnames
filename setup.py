#!/usr/bin/env python3
import os, sys
import fixnames
from fixnames import __version__, __description__, __author__, __email__, __license__
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

s = setup(
	name='fixnames',
	version=__version__,
	license=__license__,
	description=__description__,
	long_description=read("README.md"),
	long_description_content_type='text/markdown',
	keywords="utility,linux,windows",
	url='https://github.com/prahladyeri/fixnames',
	packages=find_packages(),
	include_package_data=True,
	entry_points={
		"console_scripts": [
			"fixnames = fixnames.fixnames:main",
		],
	},
	install_requires=['requests'],
	author=__author__,
	author_email=__email__,
	)


# ~ from distutils.core import setup
# ~ s = setup(name='fixnames',
	# ~ version="0.1",
	# ~ description='Utility to scan and fix filenames with special characters by renaming them.',
	# ~ license='MIT',
	# ~ author='Prahlad Yeri',
	# ~ author_email='prahladyeri@yahoo.com',
	# ~ url='https://github.com/prahladyeri/fixnames',
	# ~ #py_modules=['hotspotd','cli'],
	# ~ packages=['fixnames'],
	# ~ package_dir={'fixnames': ''},
	# ~ package_data={'fixnames': ['./']},
	# ~ scripts=['./fixnames']
	# ~ #data_files=[('config',['run.dat'])],
	# ~ )
