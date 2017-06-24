from ctypes import *

mylib = CDLL('/home/yanxurui/test/keepcoding/python/extension/ctypes/libadd.so')
# or
# mylib = cdll.LoadLibrary("/home/yanxurui/test/keepcoding/python/extension/ctypes/libadd.so")
add = mylib.add
add.argtypes = [c_int, c_int]

r = add(1, 2)
print(r)
