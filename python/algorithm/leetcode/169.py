# https://leetcode.com/problems/majority-element/discuss/51613/O(n)-time-O(1)-space-fastest-solution

class Solution:
    def majorityElement(self, nums) -> int:
        count = 0
        for i in nums:
            if count == 0:
                major = i
                count += 1
            elif major == i:
                count += 1
            else:
                count -= 1
        return major


if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            ([3,2,3]),
            3
        ),
        (
            ([2,2,1,1,1,2,2]),
            2
        )
    ]
    test(Solution().majorityElement, test_data)
