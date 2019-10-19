# https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/76959/JAVA-Easy-Version-To-Understand!!!!!!!!!!!!!!!!!
import string
from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = {}
        for c,i in zip(string.ascii_lowercase, range(1,27)):
            d[c] = i
        codes = []
        for w in words:
            v = 0
            for c in w:
                v |= (1 << d[c])
            codes.append(v)
        rst = 0
        l = len(words)
        for i in range(l):
            w1 = words[i]
            for j in range(i+1, l):
                w2 = words[j]
                if (codes[i] & codes[j]) == 0 and len(w1)*len(w2) > rst:
                    rst = len(w1)*len(w2)
        return rst



if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ["abcw","baz","foo","bar","xtfn","abcdef"],
            16
        ),
        (
            ["a","ab","abc","d","cd","bcd","abcd"],
            4
        ),
        (
            ["a","aa","aaa","aaaa"],
            0
        )
    ]
    test(Solution().maxProduct, test_data)
