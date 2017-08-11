#!/usr/bin/env
# coding=utf-8

# https://stackoverflow.com/a/14981125/6088837
from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

print('out')
eprint('err')
sys.exit(1)
