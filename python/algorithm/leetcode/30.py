# https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/13656/An-O(N)-solution-with-detailed-explanation

from collections import defaultdict

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ans = []
        n = len(s)
        cnt = len(words)
        if n==0 or cnt==0:
            return ans

        wl = len(words[0])
        d = defaultdict(int)
        for w in words:
            d[w] += 1
        import pdb
        # pdb.set_trace()
        for i in range(wl):
            left = i
            count = 0
            d2 = defaultdict(int)
            for j in range(i, n, wl):
                w = s[j:j+wl]
                if w in d: # valid word
                    d2[w] += 1
                    count += 1
                    while d2[w] > d[w]: # advance the window left side
                        w2 = s[left:left+wl]
                        d2[w2] -= 1
                        count -= 1
                        left += wl
                    if count == cnt: # find one concatenation
                        ans.append(left)
                        # advance one word
                        d2[s[left:left+wl]] -= 1
                        count -= 1
                        left += wl
                else:
                    count = 0
                    d2 = defaultdict(int)
                    left = j + wl
        return ans

    
if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ("barfoothefoobarman", ["foo","bar"]),
            [0,9]
        ),
        (
            ("wordgoodgoodgoodbestword", ["word","good","best","word"]),
            []
        ),
        (
            ("barfoofoobarthefoobarman", ["bar","foo","the"]),
            [6, 9, 12]
        )
    ]
    test(Solution().findSubstring, test_data)
