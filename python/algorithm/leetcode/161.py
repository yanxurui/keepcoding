# https://leetcode.com/problems/one-edit-distance/solutions/50098/my-clear-java-solution-with-explanation/
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        # always s shorter than t
        if m > n:
            return self.isOneEditDistance(t, s)
        assert m <= n
        if n - m > 1:
            return False
        for i in range(m):
            if s[i] != t[i]:
                if m == n:
                    # the remaining is the same
                    return s[i+1:] == t[i+1:]
                else:
                    # the only possibility is to remove a char from t
                    return s[i:] == t[i+1:]
        # remove the last char from t
        return n > m

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                "ab",
                "acb"
            ),
            True
        ),

        (
            (
                "",
                ""
            ),
            False
        )
    ]
    test(Solution().isOneEditDistance, test_data)
