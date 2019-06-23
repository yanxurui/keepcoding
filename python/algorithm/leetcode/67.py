class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l1 = len(a)
        l2 = len(b)
        i = 1
        ans = []
        s = 0
        import pdb
        # pdb.set_trace()
        while i <= l1 or i <= l2:
            if i <= l1:
                s += int(a[-i])
            if i <= l2:
                s += int(b[-i])

            if s == 0:
                ans.append('0')
            elif s == 1:
                ans.append('1')
                s = 0
            elif s == 2:
                ans.append('0')
                s = 1
            elif s == 3:
                ans.append('1')
                s = 1
            else:
                assert False
            i += 1
        if s == 1:
            ans.append('1')
        return ''.join(ans[::-1])

        
if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            (
                "11",
                "1"
            ),
            "100"
        ),
        (
            (
                "1010",
                "1011"
            ),
            "10101"
        ),

    ]
    test(Solution().addBinary, test_data)
