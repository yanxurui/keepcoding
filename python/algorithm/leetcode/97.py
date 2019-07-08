class Solution(object):
    def recursive(self, s1, s2, s3, l1, l2, l3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if l3 == 0:
            return True
        yes = self.table.get((l1, l2, l3), None)
        if yes is not None:
            return yes
        if (l1 > 0 and s3[l3-1] == s1[l1-1] and self.recursive(s1, s2, s3, l1-1, l2, l3-1)) or \
           (l2 > 0 and s3[l3-1] == s2[l2-1] and self.recursive(s1, s2, s3, l1, l2-1, l3-1)):
            yes = True
        else:
            yes = False
        self.table[(l1, l2, l3)] = yes
        return yes

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        self.table = dict()
        return self.recursive(s1, s2, s3, len(s1), len(s2), len(s3))


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                "aabcc",
                "dbbca",
                "aadbbcbcac"
            ),
            True
        ),
        (
            
            (
                "aabcc",
                "dbbca",
                "aadbbbaccc"
            ),
            False
        )
    ]
    test(Solution().isInterleave, test_data)

