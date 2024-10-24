import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        h = [] # end time
        for i in sorted(intervals, key=lambda i:i[0]):
            if h and i[0] >= h[0]:
                # can share the same room
                heapq.heappop(h)
                heapq.heappush(h, i[1])
            else:
                # need a new room
                heapq.heappush(h, i[1])
        return len(h)

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [[0,30],[5,10],[15,20]],
            2
        ),
        (
            [[7,10],[2,4]],
            1
        ),
    ]
    test(Solution().minMeetingRooms, test_data)

