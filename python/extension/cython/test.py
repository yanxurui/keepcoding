from time import time
from add_wrapper import add

s=time()
for i in range(10000000):
    r = add(i, i)
print(time()-s)
