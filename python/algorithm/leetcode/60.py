class Solution(object):
    def recursive(self, s, k):
        if k == 0:
            return
        fact = 1
        for i in range(2, len(s)+1):
            if fact*i > k:
                j = i - k//fact
                # s[-i], s[-j] = s[-j], s[-i] # swap
                s.insert(-(i-1), s.pop(-j))
                self.recursive(s, k%fact)
                return
            else:
                fact *= i


    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = [str(i) for i in range(1, n+1)]
        import pdb
        # pdb.set_trace()
        self.recursive(ans, k-1)
        return ''.join(ans)


if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            (
                3,
                3
            ),
            "213"
        ),
        (
            (
                4,
                9
            ),
            "2314"
        ),
        (
            (
                4,
                12
            ),
            "2431"
        ),
        (
            (
                3,
                5
            ),
            "312"
        )
    ]
    test(Solution().getPermutation, test_data)
