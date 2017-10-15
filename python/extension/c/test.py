from time import time
from demo import add

s=time()
for i in range(1,10000000):
    r = add(i, i)
print(time()-s)
