# https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation

class Solution(object):
    def isPalindrome(self, s):
        return s == s[::-1]

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        rst = []
        d = {w:i for i,w in enumerate(words)}
        for w, i in d.items():
            k = len(w)
            for j in range(k+1):
                prefix = w[:j]
                suffix = w[j:]
                if self.isPalindrome(prefix):
                    front = suffix[::-1]
                    if front != w and front in d:
                        rst.append([d[front], i])
                if j < k and self.isPalindrome(suffix):
                    back = prefix[::-1]
                    if back != w and back in d:
                        rst.append([i, d[back]])
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            ["abcd","dcba","lls","s","sssll"],
            [[0,1],[1,0],[3,2],[2,4]]
        ),
        (
            ["bat","tab","cat"],
            [[0,1],[1,0]]
        ),
        (
            ["abc"],
            []
        ),
    ]
    test(Solution().palindromePairs, test_data, compare=unordered_equal)
