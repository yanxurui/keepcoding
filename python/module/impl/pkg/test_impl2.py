import imp
import importlib
import os
import sys
import bar

if len(sys.argv)>1:
    custom_config_file = sys.argv[1]

    # method2: modify Python Path then import
    sys.path.insert(1, os.path.dirname(os.path.abspath(custom_config_file)))
    config=importlib.import_module(os.path.splitext(os.path.basename(custom_config_file))[0])

print(config.a)
print(config.b)
