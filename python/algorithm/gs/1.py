from collections import defaultdict, Counter

def maxLCS(s):
    # Write your code here
    rst = prev = 0
    d1 = defaultdict(int)
    d2 = Counter(s)
    for c in s:
        prev -= min(d1[c], d2[c])
        d1[c] += 1
        d2[c] -= 1
        prev += min(d1[c], d2[c])
        if prev > rst:
            rst = prev
    return rst


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            'abcdecdefg',
            3
        ),
        (
            'zzzxxxzzz',
            4
        ),
        (
            '',
            0
        ),
        (
            'a',
            0
        )
    ]
    test(maxLCS, test_data)
