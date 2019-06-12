#!/usr/bin/env python3
"""
	Utility to scan and fix filenames with special characters by renaming them.
"""
from fixnames import __title__, __version__, __description__
import os
import re
import shutil
import argparse

#specialchars = r"|\\?*<\":>+\[\]/\'"
#specialchars = r"|\\?*<\":>\[\]/"
specialchars = r"|\\?*<\":>/"
pattern = r'^.*[' + specialchars + '].*$'


def fix_names(tpath, dry_run=False):
	cnt = 0 #files
	cntd = 0 #directories
	dirs_cache = []
	print("renaming files")
	for root, dirs, files in os.walk(tpath):
		for filename in files:
			m = re.match(pattern, filename)
			if m != None:
				ofname = os.path.join(root, filename)
				nfname = filename
				for c in specialchars: nfname = nfname.replace(c,"")
				nfname = os.path.join(root, nfname)
				if not dry_run: shutil.move(ofname, nfname)
				# ~ print("root: ", root)
				# ~ print("filename: ", filename)
				print("renamed %s to %s" % (ofname,  nfname))
				cnt += 1
		for filename in dirs:
			m = re.match(pattern, filename)
			if m != None:
				ofname = os.path.join(root, filename)
				nfname = filename
				for c in specialchars: nfname = nfname.replace(c,"")
				nfname = os.path.join(root, nfname)
				#if not dry_run: shutil.move(ofname, nfname)
				#print("Added folder to rename cache: %s to %s" % (ofname,  nfname))
				dirs_cache.append([ofname, nfname])
				cntd += 1
	if len(dirs_cache) > 0: print("\nrenaming directories")
	for dd in dirs_cache:
		if not dry_run: shutil.move(dd[0], dd[1])
		print("renamed %s to %s" % (dd[0], dd[1]))
	
	print("\n%d files renamed" % cnt)
	print("%d directories renamed" % cntd)
	#print(dirs_cache)


def main():
	banner = """%s version %s
%s

Copyright (c) 2019 Prahlad Yeri. All rights reserved.

This work is licensed under the terms of the MIT license.  
For a copy, see <https://opensource.org/licenses/MIT>.
""" % (__title__, __version__, __description__)
	print(banner)
	parser = argparse.ArgumentParser(description = "Fix Filenames")
	parser.add_argument('path', help='path to the directory')
	parser.add_argument('-v', '--version', help='display version', action='store_true')
	parser.add_argument('-n', '--dry-run', help='just display results instead of actually renaming files', action='store_true')
	args = parser.parse_args()
	
	if args.version:
		sys.exit()
	
	if not (os.path.exists(args.path) and os.path.isdir(args.path)):
		print("Not a directory")
		exit()
	fix_names(args.path, args.dry_run)

if __name__ == "__main__":
	main()
