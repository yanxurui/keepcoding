class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = range(1, 10)
        ans = []
        if len(candidates) == 0:
            return ans
        self.backtrack(candidates, ans, list(), n, k, 0)
        return ans

    def backtrack(self, nums, ans, tmp, remain, k, start):
        if k == 0:
            if remain == 0:
                ans.append(tmp)
            else:
                return
        elif remain < 0:
            return
        else:
            for i in range(start, len(nums)):
                tmp.append(nums[i])
                self.backtrack(nums, ans, list(tmp), remain-nums[i], k-1, i+1)
                tmp.pop()


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            (
                3, 7
            ),
            [[1,2,4]]
        ),
        (
            (
                3, 9
            ),
            [[1,2,6], [1,3,5], [2,3,4]]
        )
    ]
    test(Solution().combinationSum3, test_data)
