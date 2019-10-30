class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        diff = []
        max_up = 0
        k = 0
        s = 0
        for i in range(n):
            d = gas[i] - cost[i]
            diff.append(d)
            # find the minimum point
            if -s > max_up:
                max_up = -s
                k = i
            s += d

        s = 0
        for j in range(n):
            m = (k+j) % n
            s += diff[m] 
            if s < 0:
                return -1
        return k



import sys
INT_MAX = sys.maxsize
class Solution2(object):
    def canCompleteCircuit(self, gas, cost):
        left = 0
        min_left = INT_MAX
        for i in range(len(gas)):
            if left < min_left:
                k = i
                min_left = left
            left += (gas[i] - cost[i])
        # if left - min_left + min_left >= 0:
        if left >= 0:
            return k
        else:
            return -1



if __name__ == '__main__':
    from testfunc import test
    test_data = [  
        (
            (
                [1,2,3,4,5],
                [3,4,5,1,2]
            ),
            3
        ),
        (
            (
                [2,3,4],
                [3,4,3]
            ),
            -1
        ),
    ]
    test(Solution2().canCompleteCircuit, test_data)
