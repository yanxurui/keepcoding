# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/solutions/927549/c-java-python-3-greedy/
import collections

class Solution:
    def minDeletions(self, s: str) -> int:
        counter = collections.Counter(s)
        usedFreq = set()        
        ans = 0
        for _, freq in counter.items():
            while freq > 0 and freq in usedFreq:
                freq -= 1
                ans += 1
            usedFreq.add(freq)
        return ans

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            'aab',
            0
        ),
        (
            'aaabbbcc',
            2
        ),
        (
            'ceabaacb',
            2
        )
    ]
    test(Solution().minDeletions, test_data)

