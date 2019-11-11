import sys
from collections import OrderedDict, defaultdict

d = OrderedDict()
n = int(sys.stdin.readline())

for line in sys.stdin:
	line.rstrip()
	if not line:
		break
	# print(line)
	fruit, worker, weight = line.split()
	if fruit not in d:
		d[fruit] = defaultdict(int)
	d[fruit][int(worker)] += int(weight)


def compare(x, y):
	if x[1] == y[1]:
		return x[0] - y[0]
	else:
		return x[1] - y[1]
for k, v in d.items():
	for worker, weight in sorted(v.items(), cmp=compare):
		print('%s %d %d' % (k, worker, weight))



