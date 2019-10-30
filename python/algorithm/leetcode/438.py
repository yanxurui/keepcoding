# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.
from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        cnt = len(count)
        rst = []
        i = j = 0
        while j < len(s):
            if s[j] in count:
                count[s[j]] -= 1
                if count[s[j]] == 0:
                    cnt -= 1
            j += 1
            # make it invalid
            while cnt == 0:
                if j - i == len(p):
                    rst.append(i)
                if s[i] in count:
                    count[s[i]] += 1
                    if count[s[i]] > 0:
                        cnt += 1
                i += 1
        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                'cbaebabacd',
                'abc'
            ),
            [0, 6]
        ),
        (
            (
                'abab',
                'ab'
            ),
            [0, 1, 2]
        ),
        (
            (
                'ab',
                'abc'
            ),
            []
        ),
    ]
    test(Solution().findAnagrams, test_data)
