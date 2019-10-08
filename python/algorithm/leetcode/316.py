# https://leetcode.com/problems/remove-duplicate-letters/discuss/76768/A-short-O(n)-recursive-greedy-solution

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = Counter(s)
        pos = 0
        for i, c in enumerate(s):
            cnt[c] -= 1
            if c < s[pos]:
                pos = i
            if cnt[c] == 0:
                break
        return '' if not s else s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ''))



if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ('bcabc'),
            'abc'
        ),
        (
            ('cbacdcbc'),
            'acdb'
        )
    ]
    test(Solution().removeDuplicateLetters, test_data)
