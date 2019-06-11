# https://leetcode.com/problems/permutations-ii/discuss/18602/9-line-python-solution-with-1-line-to-handle-duplication-beat-99-of-others-%3A-)

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for n in nums:
            new_ans = []
            for an in ans:
                for i in range(len(an)+1):
                    new_ans.append(an[:i]+[n]+an[i:])
                    if i < len(an) and an[i] == n:
                        break
            ans = new_ans
        return ans


if __name__ == '__main__':
    from testfunc import test

    def compare(a, b):
        '''compare 2 nested list without order
        '''
        return len(a) == len(b) and sorted(a) == sorted(b)

    test_data = [
        (
            [1,1,2],
            [
                [1,1,2],
                [1,2,1],
                [2,1,1]
            ]
        ),
        (
            [1,2,3,1],
            [
                [1,1,2,3],
                [1,1,3,2],
                [1,2,1,3],
                [1,2,3,1],
                [1,3,1,2],
                [1,3,2,1],
                [2,1,1,3],
                [2,1,3,1],
                [2,3,1,1],
                [3,1,1,2],
                [3,1,2,1],
                [3,2,1,1]
            ]
        )
    ]
    test(Solution().permuteUnique, test_data, compare=compare)

