from time import time
from ctypes import *

mylib = CDLL('/home/yanxurui/test/keepcoding/python/extension/ctypes/libadd.so')
add = mylib.add
add.argtypes = [c_int, c_int]

s=time()
for i in range(10000000):
    r = add(i, i)
print(time()-s)
