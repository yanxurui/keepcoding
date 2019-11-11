import sys
from collections import defaultdict
d = defaultdict(int)
for line in sys.stdin:
    k, v = line.split(',')
    d[k] += int(v)
rst = 0
for k, v in d.items():
    if v >= 10:
        rst += 1
print(rst)
