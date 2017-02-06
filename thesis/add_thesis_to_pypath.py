#!/usr/bin/python3
### -----------------------------------------------------------------
"""
A few lines of code that adds the thesis directory (relative to the
home directory on my laptop) to the pythonpath.  The purpose of this
is to create a way of running scripts needing the thesis modules
easily without having to put machine specific headers at the top of files

has one function which reads in the list of added paths and inserts them
onto syspath
"""
### -----------------------------------------------------------------

import sys

pathfile = "pathsto"

def add_paths():
    f = open(pathfile,"r")
    for line in f:
        sys.path.insert(0,line.strip())


if __name__ == "__main__":
    add_paths()
