#!/usr/bin/env python3

import sys
import os.path
import argparse
from pathlib import Path
import pyperclip
from binaryornot.check import is_binary

# arguments
parser = argparse.ArgumentParser(description='Copy the contents of a file to the clipboard.')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.0.1')
parser.add_argument('filename', help='the file to read')
args = parser.parse_args()

# does the file exist?
filename_exists = os.path.exists(args.filename)

if filename_exists is False:
    print("Error: The input file doesn't exist.")
    sys.exit(1)

# make sure the file is an ascii text file
if is_binary(args.filename):
    print("Error: The input file is non-text.")
    sys.exit(1)
else:
    # read file and put into var
    contents = Path(args.filename).read_text()
    # remove trailing newline
    contents = contents.rstrip("\n")
    # copy contents to clipboard
    pyperclip.copy(contents)

# verify the copy
if contents != pyperclip.paste():
    print("Error: The file was not copied to the clipboard.")
    sys.exit(1)
