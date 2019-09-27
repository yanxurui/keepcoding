class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            res = res + (n % 2)
            n = n >> 1
        return res

        
if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            (int('00000000000000000000000000001011', 2)),
            3
        ),
        (
            (int('00000000000000000000000010000000', 2)),
            1
        ),
        (
            (int('11111111111111111111111111111101', 2)),
            31
        ),
    ]
    test(Solution().hammingWeight, test_data)
