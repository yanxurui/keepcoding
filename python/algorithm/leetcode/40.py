class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        if len(candidates) == 0:
            return ans
        self.backtrack(candidates, ans, list(), target, 0)
        return ans

    def backtrack(self, nums, ans, tmp, remain, start):
        if remain < 0:
            return
        elif remain == 0:
            ans.append(list(tmp))
        else:
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]: # skip duplicate
                    continue
                tmp.append(nums[i])
                self.backtrack(nums, ans, tmp, remain-nums[i], i+1) # i+1
                tmp.pop()


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ([10,1,2,7,6,1,5], 8),
            [
                [1, 1, 6],
                [1, 2, 5],
                [1, 7],
                [2, 6]
            ]
        ),
        (
            ([2,5,2,1,2], 5),
            [
                [1,2,2],
                [5]
            ]
        ),
        (
            ([1],1),
            [
                [1]
            ]
        )
    ]
    test(Solution().combinationSum2, test_data)
