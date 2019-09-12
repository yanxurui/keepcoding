# https://leetcode.com/problems/palindrome-partitioning/discuss/41963/Java%3A-Backtracking-solution.

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        tmp = []
        self.dfs(s, 0, tmp, res)
        return res

    def dfs(self, s, b, tmp, res):
        if b == len(s):
            res.append(list(tmp))
        else:
            for e in range(b+1, len(s)+1):
                if self.ispal(s[b:e]):
                    tmp.append(s[b:e])
                    self.dfs(s, e, tmp, res)
                    tmp.pop()
    
    def ispal(self, s):
        l = len(s)
        for i in range(l//2):
            if s[i] != s[l-i-1]:
                return False
        return True


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            ("aab"),
            [
              ["aa","b"],
              ["a","a","b"]
            ]
        )
    ]
    test(Solution().partition, test_data, compare=unordered_equal)
