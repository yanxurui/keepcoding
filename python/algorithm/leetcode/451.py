from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        r = []
        for char,count in sorted(d.items(), key=lambda item: -item[1]):
            r.append(char * count)
        return ''.join(r)

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            'tree',
            'eetr'
        ),
        (
            'cccaaa',
            'cccaaa'
        ),
        (
            'Aabb',
            'bbAa'
        )
    ]
    test(Solution().frequencySort, test_data)
