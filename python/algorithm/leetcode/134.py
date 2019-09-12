class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        diff = []
        for i in range(n):
            diff.append(gas[i] - cost[i])
        for i in range(n):
            if diff[i] >= 0:
                s = diff[i]
                for j in range(1, n):
                    k = (i+j) % n
                    s += diff[k]
                    if s < 0:
                        break
                if s >= 0:
                    return i
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
    test(Solution().canCompleteCircuit, test_data)
