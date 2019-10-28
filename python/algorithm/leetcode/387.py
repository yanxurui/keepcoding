# https://leetcode.com/problems/two-sum/discuss/17/Here-is-a-Python-solution-in-O(n)-time
from typing import List
from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = Counter(s)
        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            'leetcode',
            0
        ),
        (
            'loveleetcode',
            2
        ),
    ]
    test(Solution().firstUniqChar, test_data)

