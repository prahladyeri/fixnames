# Introduction
*fixnames* is a utility to scan and fix linux filenames with special characters by renaming them.

# Synopsis

Linux is liberal in letting us choose filenames, so sometimes we end up choosing files with special characters such as `|, [, ], etc`. When you try to use these files on other operating systems like Windows or Android, they fail to work properly. `fixnames` is a Python utility to scan and fix such files on your linux system. `fixnames` scans files recursively in a given directory and fixes them by renaming if found to contain special chars.

# Installation
```
pip install fixnames
```

# Uninstallation
```
pip uninstall fixnames
```

# Usage
```
$ fixnames ./

renaming files

renaming directories
renamed ./test/bing" to ./test/bing

0 files renamed
1 directories renamed
```

# Notes

According to [Wikipedia](https://en.wikipedia.org/wiki/Filename#Comparison_of_filename_limitations), these are the special characters which aren't allowed on NTFS file systems:

	0x00-0x1F 0x7F " * / : < > ? \ |
	
