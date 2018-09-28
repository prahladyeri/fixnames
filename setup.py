#!/usr/bin/env python3
import os
import sys

def uninstall_parts(package):
	pass
	#~ import shutil
	#~ #sys.prefix
	#~ loc=os.sep.join([sys.prefix, 'lib', 'python' + sys.version[:3], 'site-packages', package]) #try sys.prefix
	#~ if os.path.exists(loc):
		#~ print('Removing files from ' + loc)
		#~ shutil.rmtree(loc,ignore_errors=False)
	#~ loc=os.sep.join([sys.prefix, 'lib', 'python' + sys.version[:3], 'dist-packages', package]) #try dist-packages
	#~ if os.path.exists(loc):
		#~ print('Removing files from ' + loc)
		#~ shutil.rmtree(loc,ignore_errors=False)
	
	#~ #/usr/local
	#~ loc=os.sep.join(['/usr/local', 'lib', 'python' + sys.version[:3], 'site-packages', package]) #try sys.prefix
	#~ if os.path.exists(loc):
		#~ print('Removing files from ' + loc)
		#~ shutil.rmtree(loc,ignore_errors=False)
	#~ loc=os.sep.join(['/usr/local', 'lib', 'python' + sys.version[:3], 'dist-packages', package]) #try dist-packages
	#~ if os.path.exists(loc):
		#~ print('Removing files from ' + loc)
		#~ shutil.rmtree(loc,ignore_errors=False)
		
	#~ if os.path.exists('/usr/local/bin/' + package):
		#~ print('Removing file: /usr/local/bin/' + package)
		#~ try: os.remove('/usr/local/bin/' + package)
		#~ except: pass
	#~ if os.path.exists('/usr/bin/' + package):
		#~ print('Removing file: /usr/bin/' + package)
		#~ try: os.remove('/usr/bin/' + package)
		#~ except: pass
	#~ if os.path.islink('/usr/bin/' + package):
		#~ print('Removing link: /usr/bin/' + package)
		#~ try: os.remove('/usr/bin/' + package)
		#~ except: pass

if 'uninstall' in sys.argv:
	print('Uninstall complete')
	sys.exit(0)

#INSTALL IT
#the_version = open("VERSION").read().strip()
from distutils.core import setup
s = setup(name='fixnames',
	version="0.1",
	description='Utility to scan and fix filenames with special characters by renaming them.',
	license='MIT',
	author='Prahlad Yeri',
	author_email='prahladyeri@yahoo.com',
	url='https://github.com/prahladyeri/fixnames',
	#py_modules=['hotspotd','cli'],
	packages=['fixnames'],
	package_dir={'fixnames': ''},
	package_data={'fixnames': ['./']},
	scripts=['./fixnames']
	#data_files=[('config',['run.dat'])],
	)
