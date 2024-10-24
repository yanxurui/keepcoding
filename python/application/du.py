#!/usr/bin/env python
# coding=utf-8

import os
import sys
import pdb
from os import path
import argparse

class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    pass
parser = argparse.ArgumentParser(
    description="find the biggest folder(excluding sub folders)",
    formatter_class=CustomFormatter,
    epilog='''example:
  python du.py ~ 104857600
''')
parser.add_argument('top',
    help='starting directory',
    nargs='?',
    default='./')
parser.add_argument('limit',
    help='only print folders whose size are bigger than this number(bytes)',
    nargs='?',
    default=1024*1024,
    type=int)
parser.add_argument('-b', '--byte',
    help='output size in bytes instead of human readable output',
    action='store_true')
args = parser.parse_args()

folders = {}

def human_readable_size(size):
    if size / 1024 > 0:
        size = size / 1024
        if size / 1024 > 0:
            size = size /1024
            if size / 1024 > 0:
                size = "%dG" % (size/1024)
            else:
                size= "%dM" % size
        else:
            size = "%dK" % size
    return size

# count the number of bytes taken by non-directory files in each directory under the starting directory
for root, dirs, files in os.walk(args.top):
    # print(root, sum(getsize(join(root, name)) for name in files))
    # By default, walk() will not walk down into symbolic links that resolve to directories
    size = 0
    for name in files:
        if path.islink(path.join(root, name)):
            continue
        file = path.join(root, name)
        if file == '/proc/kcore':
            continue
        try:
            size += path.getsize(file)
        except OSError as e:
            print(e)
    folders[root] = size

for path in sorted(folders, key=folders.get, reverse=True):
    if folders[path] < args.limit:
        break
    size = folders[path]
    if not args.byte:
        print("%s\t\t%s" % (human_readable_size(size), path))
    else:
        print("%s\t\t%s" % (size, path))
