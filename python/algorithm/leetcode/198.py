class Solution(object):
    # def rob(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     n = len(nums)
    #     if n == 0:
    #         return 0
    #     tab = [0] * n
    #     for i in range(n):
    #         if i == 0 or i == 1:
    #             tab[i] = nums[i]
    #         for j in range(i-1):
    #             if tab[j] + nums[i] > tab[i]:
    #                 tab[i] = tab[j] + nums[i]
    #     return max(tab)

    # https://leetcode.com/problems/house-robber/discuss/55681/Java-O(n)-solution-space-O(1)
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pN = pY = 0 # the max amount of money he can get by rob the current house or not
        for n in nums:
            tmp = pN
            pN = max(pN, pY)
            pY = tmp + n
        return max(pN, pY)


if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            ([1,2,3,1]),
            4
        ),
        (
            ([2,7,9,3,1]),
            12
        ),
        (
            ([]),
            0
        )
    ]
    test(Solution().rob, test_data)
