class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for n in nums:
            l = len(ans)
            for i in range(l):
                ans.append(ans[i]+[n])
        return ans


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            [1,2,3],
            [
                [3],
                [1],
                [2],
                [1,2,3],
                [1,3],
                [2,3],
                [1,2],
                []
            ]
        )
    ]
    test(Solution().subsets, test_data, compare=unordered_equal)
