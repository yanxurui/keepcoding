# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/108730/JavaC%2B%2BStraightforward-dfs-solution
from typing import List
# TLE
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        seen = [False] * len(nums)
        nums.sort()
        import pdb
        pdb.set_trace()
        return k >= 1 and s % k == 0 and self.canPartition(nums, seen, 0, k, 0, s//k)

    def canPartition(self, nums, seen, startIndex, k, cum_sum, target):
        print(startIndex)
        if k == 1:
            return True
        if cum_sum == target:
            return self.canPartition(nums, seen, 0, k-1, 0, target)
        else:
            for i in range(startIndex, len(nums)):
                if seen[i]:
                    continue
                if cum_sum + nums[i] > target:
                    break
                seen[i] = True
                if self.canPartition(nums, seen, i+1, k, cum_sum+nums[i], target):
                    return True
                else:
                    seen[i] = False
            return False



# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/140541/Clear-explanation-easy-to-understand-C%2B%2B-%3A-4ms-beat-100
class Solution2:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        nums.sort(reverse=True)
        return k >= 0 and s % k == 0 and self.put(nums, 0, [0]*k, s//k)
    def put(self, nums, i, buckets, target):
        # put nums[i] in some bucket
        if i == len(nums):
            return True
        for j in range(len(buckets)):
            if nums[i] + buckets[j] > target:
                continue
            buckets[j] += nums[i]
            # put next num
            if self.put(nums, i+1, buckets, target):
                return True
            else:
                # take it out
                buckets[j] -= nums[i]
                if buckets[j] == 0:
                    # no need to try other empty buckets
                    return False
        return False

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [4, 3, 2, 3, 5, 2, 1],
                4
            ),
            True
        ),
        (
            (
                [2,2,2,2,3,4,5],
                4,
            ),
            False
        ),
        (
            (
                [4,5,3,2,5,5,5,1,5,5,5,5,3,5,5,2],
                13
            ),
            True
        ),
        (
            (
                [18,20,39,73,96,99,101,111,114,190,207,295,471,649,700,1037],
                4
            ),
            True
        ),
    ]
    test(Solution2().canPartitionKSubsets, test_data)

