class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not len(s) == len(t):
            return False
        m = {}
        v = set()
        for c1,c2 in zip(s, t):
            to = m.get(c1)
            if to:
                if to != c2:
                    return False
            else:
                if c2 in v:
                    return False
                m[c1] = c2
                v.add(c2)
        return True



if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            ("egg", 'add'),
            True
        ),
        (
            ('foo', 'bar'),
            False
        ),
        (
            ('paper', 'title'),
            True
        ),
        (
            ('ab', 'aa'),
            False
        )
    ]
    test(Solution().isIsomorphic, test_data)
