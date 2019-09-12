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
    test(Solution().canCompleteCircuit, test_data)
