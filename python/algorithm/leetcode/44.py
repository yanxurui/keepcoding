# https://leetcode.com/problems/wildcard-matching/discuss/17810/Linear-runtime-and-constant-space-solution

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i, j = 0, 0
        star, ss = None, None
        s += ' '
        p += ' '
        import pdb
        # pdb.set_trace()
        while s[i] != ' ':
            if s[i] == p[j] or p[j] == '?':
                # match or pattern is ?
                # advance both string and pattern
                i += 1
                j += 1
            elif p[j] == '*':
                # not match, pattern is *
                # only advance pattern
                star = j
                j += 1
                ss = i
            elif star is not None:
                # not match, last pattern is *, current pattern is not *
                # only advance string
                j = star + 1
                ss += 1
                i = ss
            else:
                # not match, last pattern is not *, current pattern is not *
                # failed
                return False

        while p[j] == '*':
            j += 1
        return p[j] == ' '


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ("aa", "a"),
            False
        ),
        (
            ("aa", "*"),
            True
        ),
        (
            ("cb", "?a"),
            False
        ),
        (
            ("adceb", "*a*b"),
            True
        ),
        (
            ("acdcb", "a*c?b"),
            False
        ),

        (
            ("acdcb", "a*cb"),
            True
        ),
        (
            ("ababababab", "*ab"),
            True
        ),
        (
            ("aaaaaaa", "*a"),
            True
        )
    ]
    test(Solution().isMatch, test_data)

