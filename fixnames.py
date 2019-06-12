#!/usr/bin/env python3
"""
	Utility to scan and fix filenames with special characters by renaming them.
"""
import os
import re
import shutil
import argparse

specialchars = r"|\\?*<\":>+\[\]/\'"
pattern = r'^.*[' + specialchars + '].*$'

def fix_names(tpath):
	for root, dirs, files in os.walk(tpath):
		for filename in files:
			m = re.match(pattern, filename)
			if m != None:
				ofname = os.path.join(root, filename)
				nfname = filename
				for c in specialchars:
					nfname = nfname.replace(c,"")
				nfname = os.path.join(root, nfname)
				shutil.move(ofname, nfname)
				print("Renamed: %s to %s" % (ofname,  nfname))


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description = "Fix Filenames")
	parser.add_argument('scandir', help='scan directory')
	args = parser.parse_args()
	if not (os.path.exists(args.scandir) and os.path.isdir(args.scandir)):
		print("Not a directory")
		exit()
	fix_names(args.scandir)
	print("Done")
