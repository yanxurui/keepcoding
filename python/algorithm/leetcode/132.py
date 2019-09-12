# https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42198/My-solution-does-not-need-a-table-for-palindrome-is-it-right-It-uses-only-O(n)-space.

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cut = {}
        for i in range(n+1):
            cut[i] = i - 1

        for i in range(n):
            # odd
            j = 0 # important
            while i-j >=0 and i+j < n and s[i-j] == s[i+j]:
                cut[i+j+1] = min(cut[i+j+1], cut[i-j]+1)
                j += 1
            
            # even
            j = 1
            while i-j+1 >=0 and i+j < n and s[i-j+1] == s[i+j]:
                cut[i+j+1] = min(cut[i+j+1], cut[i-j+1]+1)
                j += 1
        return cut[n]


if __name__ == '__main__':
    from testfunc import test
    test_data = [  
        (
            ("aab"),
            1
        ),
        (
            ("aaaaba"),
            1
        ),
    ]
    test(Solution().minCut, test_data)
