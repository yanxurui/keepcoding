import imp
import sys
from pprint import pprint
import bar

if len(sys.argv)>1:
    custom_config_file = sys.argv[1]
    print '+++++%s' % bar.a
    imp.load_source('bar', custom_config_file)
    print '-----%s' % bar.a

import baz

def main():
    print bar.a
    print bar.b
