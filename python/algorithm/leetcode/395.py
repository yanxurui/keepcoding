from collections import defaultdict, Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if s == '':
            return 0
        rst = 0
        count = Counter(s)
        if min(count.values()) >= k:
            return len(s)
        i = j = 0
        while j <= len(s):
            if j == len(s) or count[s[j]] < k:
                # a sep is found
                rst = max(rst, self.longestSubstring(s[i:j], k))
                i = j + 1
            j += 1
        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                'aaabb',
                3
            ),
            3
        ),
        (
            (
                'ababbc',
                2
            ),
            5
        ),
        (
            (
                "bbaaacbd",
                3
            ),
            3
        ),
    ]
    test(Solution().longestSubstring, test_data)

