# Introduction
*fixnames* is a utility to scan and fix linux filenames with special characters by renaming them.

# Synopsis

Linux is liberal in letting us choosing filenames, so sometimes we end up choosing filenames with special characters such as `|, [, ], etc`. When you later transfer these files to other operating systems like Windows or Android, they fail to work properly. `fixnames` is a Python utility to scan and fix such files on your linux system. `fixnames` scans filenames recursively in a given directory and fixes them by renaming.

# Installation
```
pip3 install fixnames
```

# Uninstallation
```pip3 uninstall fixnames```

# Usage

```
fixnames ./
Renamed: ../test[.txt to ../test.txt
Done
```
