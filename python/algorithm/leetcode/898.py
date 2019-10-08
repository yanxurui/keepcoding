# https://leetcode.com/problems/bitwise-ors-of-subarrays/discuss/165881/C%2B%2BJavaPython-O(30N)

class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res, cur = set(), set()
        for n in A:
            cur = {i | n for i in cur} | {n}
            res |= cur
        return len(res)


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ([0]),
            1
        ),
        (
            ([1,1,2]),
            3
        ),
        (
            ([1,2,4]),
            6
        )
    ]
    test(Solution().subarrayBitwiseORs, test_data)
