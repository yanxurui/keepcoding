class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda l: l[0])
        if len(intervals) == 0:
            return []
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                if intervals[i][1] <= ans[-1][1]:
                    continue
                else:
                    ans[-1][1] = intervals[i][1]
            else:
                ans.append(intervals[i])
        return ans


if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            [[1,3],[2,6],[8,10],[15,18]],
            [[1,6],[8,10],[15,18]]
        ),
        (
            [[1,4],[4,5]],
            [[1,5]]
        )
    ]
    test(Solution().merge, test_data)
