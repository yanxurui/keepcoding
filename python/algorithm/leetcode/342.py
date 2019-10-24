# https://leetcode.com/problems/power-of-four/discuss/80457/Java-1-line-(cheating-for-the-purpose-of-not-using-loops)

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # return num > 0 and num&(num-1) == 0 and (num-1)%3==0
        return num > 0 and num&(num-1) == 0 and num&0x55555555!=0



if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            16,
            True
        ),
        (
            5,
            False
        ),
        (
            1,
            True
        ),
    ]
    test(Solution().isPowerOfFour, test_data)

