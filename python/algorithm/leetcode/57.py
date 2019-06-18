class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for interval in intervals:
            if interval[0] < newInterval[0]:
                if interval[1] < newInterval[0]:
                    ans.append(interval)
                elif interval[1] < newInterval[1]:
                    newInterval[0] = interval[0]
                else:
                    ans = intervals
                    break
            elif interval[0] <= newInterval[1]:
                if interval[1] <= newInterval[1]:
                    continue
                else:
                    ans.append([newInterval[0], interval[1]])
            else:
                if not (ans and ans[-1][1] >= newInterval[1]):
                    ans.append(newInterval)
                ans.append(interval)

        if not (ans and ans[-1][1] >= newInterval[1]):
            ans.append(newInterval)
        return ans


if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            (
                [[1,3],[6,9]],
                [2,5]
            ),
            [[1,5],[6,9]]
        ),
        (
            (
                [[1,2],[3,5],[6,7],[8,10],[12,16]],
                [4,8]
            ),
            [[1,2],[3,10],[12,16]]
        )
    ]
    test(Solution().insert, test_data)
