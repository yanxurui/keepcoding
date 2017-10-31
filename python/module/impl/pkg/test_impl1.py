import imp
import importlib
import os
import sys
import bar

if len(sys.argv)>1:
    custom_config_file = sys.argv[1]

    # method1: use impl
    print '+++++%s' % bar.a
    imp.load_source('bar', custom_config_file)
    print '-----%s' % bar.a

import baz

print bar.a
print bar.b
