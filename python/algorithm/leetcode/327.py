# https://leetcode.com/problems/count-of-range-sum/discuss/77991/Short-and-simple-O(n-log-n)

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        first = [0]
        for num in nums:
            first.append(first[-1]+num)

        def sort(lo, hi):
            mid = (lo + hi) // 2
            if lo == mid:
                return 0
            count = sort(lo, mid) + sort(mid, hi)
            i = j = mid
            for f in first[lo:mid]:
                while i < hi and first[i]-f < lower:
                    i += 1
                while j < hi and first[j]-f <= upper:
                    j += 1
                count += (j-i)
            first[lo:hi] = sorted(first[lo:hi])
            return count
        return sort(0, len(first))


if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            (
                [-2,5,-1],
                -2,
                2
            ),
            3
        )
    ]
    test(Solution().countRangeSum, test_data)
