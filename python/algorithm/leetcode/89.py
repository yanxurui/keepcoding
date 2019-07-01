# https://leetcode.com/problems/gray-code/discuss/29891/Share-my-solution

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0]
        for i in range(n):
            for k in range(len(ans)-1, -1, -1):
                ans.append(ans[k] | 1 << i)
        return ans


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            2,
            [0,1,3,2]
        ),
        (
            0,
            [0]
        ),
        (
            3,
            [0,1,3,2,6,7,5,4]
        )
    ]
    test(Solution().grayCode, test_data)

