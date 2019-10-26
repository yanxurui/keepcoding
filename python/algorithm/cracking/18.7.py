# -*- coding:utf-8 -*-

class LongestString:
    def getLongest(self, s, n):
        # write code here
        strs = sorted(s, key=lambda item:-len(item))
        for i, s in enumerate(strs):
            if self.cat(strs, i, s):
                return len(s)
        return 0

    def cat(self, strs, i, s):
        for j in range(i+1, len(strs)):
            sub = strs[j]
            if s == sub:
                return True
            if s.startswith(sub):
                if self.cat(strs, i, s[len(sub):]):
                    return True
        return False



if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode, ListNode
    test_data = [
        (
            (
                ["a","b","c","ab","bc","abc"],6
            ),
            3
        ),
    ]
    test(LongestString().getLongest, test_data)
