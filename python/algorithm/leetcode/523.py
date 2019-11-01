from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dp = set()
        for i in range(1, len(nums)):
            new_dp = set()
            if k == 0:
                dp.add(nums[i-1])
            else:
                dp.add((nums[i-1]%k))
            for s in dp:
                s += nums[i]
                if k==0:
                    if s == 0:
                        return True
                elif s % k == 0:
                    return True

                if k == 0:
                    new_dp.add(s)
                else:
                    new_dp.add(s%k)
            dp = new_dp
        return False

class Solution2:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:-1} 
        cum_sum = 0
        for i in range(len(nums)):
            cum_sum += nums[i]
            if k!=0:
                cum_sum %= k
            prev = d.get(cum_sum)
            if prev is not None:
                if i - prev >= 2:
                    return True
            else:
                d[cum_sum] = i
        return False



if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [23, 2, 4, 6, 7],
                6
            ),
            True
        ),
        (
            (
                [23, 2, 6, 4, 7],
                6
            ),
            True
        ),
        (
            (
                [23,2,6,4,7],
                0
            ),
            False
        ),
        (
            (
                [1, 5],
                -6
            ),
            True
        ),
    ]
    test(Solution2().checkSubarraySum, test_data)

