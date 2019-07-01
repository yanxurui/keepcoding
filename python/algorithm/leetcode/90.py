# https://leetcode.com/problems/subsets-ii/discuss/30166/Simple-python-solution-without-extra-space.

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                l = len(ans)
            for j in range(len(ans)-l, len(ans)):
                ans.append(ans[j]+[nums[i]])
        return ans


if __name__ == '__main__':
    from testfunc import test
    def sort_nest(L):
        for i in range(len(L)):
            if isinstance(L[i], list):
                L[i] = sort_nest(L[i])
        return sorted(L)

    def compare(a, b):
        '''compare 2 unordered nested list
        '''
        return len(a) == len(b) and sort_nest(a) == sort_nest(b)

    test_data = [  
        (
            [1,2,2],
            [
                [2],
                [1],
                [1,2,2],
                [2,2],
                [1,2],
                []
            ]
        )
    ]
    test(Solution().subsetsWithDup, test_data, compare=compare)
