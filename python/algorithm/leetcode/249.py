from typing import List
from collections import defaultdict

class Solution:
    def pattern(self, s):
        p = []
        for i in range(1, len(s)):
            # ord, convert 'a' o 97
            d = ord(s[i])-ord(s[i-1])
            if d < 0:
                d += 26
            p.append(d)
        return tuple(p)

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strings:
            d[self.pattern(s)].append(s)
        return list(d.values())
                            


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            ["abc","bcd","acef","xyz","az","ba","a","z"],
            [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
        )
    ]
    test(Solution().groupStrings, test_data, compare=unordered_equal)

