class Solution(object):
    def cb(self, ans, tmp, nums):
        ans.append([nums[i] for i in tmp])
        if len(tmp) == 0:
            start = 0
        else:
            start = tmp[-1]+1
        for i in range(start, len(nums)):
            self.cb(ans, tmp+[i], nums)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        mask = [1]*len(nums)
        self.cb(ans, [], nums)
        return ans


if __name__ == '__main__':
    from testfunc import test

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
    test(Solution().subsets, test_data)
