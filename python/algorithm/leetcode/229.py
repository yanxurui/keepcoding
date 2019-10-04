# https://leetcode.com/problems/majority-element-ii/discuss/63520/Boyer-Moore-Majority-Vote-algorithm-and-my-elaboration

class Solution:
    def majorityElement(self, nums):
        m1, c1 = 0, 0
        m2, c2 = 1, 0
        import pdb
        # pdb.set_trace()
        for n in nums:
            if n == m1:
                c1 += 1
            elif n == m2:
                c2 += 1
            elif c1 == 0:
                m1 = n
                c1 += 1
            elif c2 == 0:
                m2 = n
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        # filter
        return [n for n in (m1, m2) if nums.count(n) > len(nums)//3]


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            ([3,2,3]),
            [3]
        ),
        (
            ([1,1,1,3,3,2,2,2]),
            [1,2]
        )
    ]
    test(Solution().majorityElement, test_data, compare=unordered_equal)
