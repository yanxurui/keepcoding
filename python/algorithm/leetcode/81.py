# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/28218/My-8ms-C%2B%2B-solution-(o(logn)-on-average-o(n)-worst-case)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            # m = (l + r)//2
            med = nums[m]
            if med == target:
                return True
            if med == nums[l] and med == nums[r]:
                l += 1
                r -= 1
            elif med >= nums[l]:
                if target >= nums[l] and target < med:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > med and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [2,5,6,0,0,1,2],
                0
            ),
            True
        ),
        (
            (
                [2,5,6,0,0,1,2],
                3
            ),
            False
        ),
        (
            (
                [1,1,3,1],
                3
            ),
            True
        ),
        (
            (
                [1,3,1,1,1],
                3
            ),
            True
        ),
    ]
    test(Solution().search, test_data)
