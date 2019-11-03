# https://leetcode.com/problems/permutation-in-string/discuss/102588/Java-Solution-Sliding-Window
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needed = Counter(s1)
        l1 = len(s1)
        unmatched = len(needed) # how many chars that needed[c] <= 0
        for i in range(len(s2)):
            if s2[i] in needed:
                needed[s2[i]] -= 1
                if needed[s2[i]] == 0:
                    unmatched -= 1
            if i >= l1:
                j = i - l1
                if s2[j] in needed:
                    if needed[s2[j]] == 0:
                        unmatched += 1
                    needed[s2[j]] += 1
            if unmatched == 0:
                return True
        return False


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                'ab',
                'eidbaooo'
            ),
            True
        ),
        (
            (
                'ab',
                'eidboaoo'
            ),
            False
        ),
    ]
    test(Solution().checkInclusion, test_data)

