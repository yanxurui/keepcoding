# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)

class Solution(object):
    def combinationSum(self, candidates, target):
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
            ans.append(tmp)
        else:
            for i in range(start, len(nums)):
                tmp.append(nums[i])
                self.backtrack(nums, ans, list(tmp), remain-nums[i], i) # i not i+1
                tmp.pop()


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ([2,3,6,7], 7),
            [
                [2,2,3],
                [7]
            ]
        ),
        (
            ([2,3,5], 8),
            [
                [2,2,2,2],
                [2,3,3],
                [3,5]
            ]
        ),
        (
            ([1],1),
            [
                [1]
            ]
        )
    ]
    test(Solution().combinationSum, test_data)
