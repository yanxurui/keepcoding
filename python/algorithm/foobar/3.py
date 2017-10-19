import pdb

def answer(h, q):
    def solve(n, top, off):
        # pdb.set_trace()
        # assert n<=top, "%d <= %d" % (n,top)
        if n == top:
            return -1
        # right child
        right = top - 1
        # left child
        left = (top-off-1)/2 + off
        if n == left or n == right:
            return top
        if n < left:
            return solve(n, left, off)
        if n > left:
            return solve(n, right, left)
        # assert False, "n=%d"%n

    result = []
    top = (1 << h) -1
    for n in q:
        result.append(solve(n, top, 0))
    return result


for (h, q) in [
        (1,[1]),
        (2,[1,2,3]),
        (3,[1,2,3,4,5,6,7]),
        (4,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]),
        (5,[16,17,18,19,26,27,28,29,30,31])
    ]:
    print(answer(h,q))
