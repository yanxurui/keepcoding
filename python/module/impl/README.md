2 methods to import a python file from any path

1. use `impl.load_source`
test
```
python test_impl1.py ../bar.py
```

pros:

* can replace a currently imported module

cons:

* the module which is imported can not import other modules from its directory


2. modify python path then use `importlib.import_module` to import dynamicly

test
```
python test_impl2.py ../foo.py
```
