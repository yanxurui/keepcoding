class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        rst = 0
        cur = 0
        for p, s in sorted(zip(position, speed), key=lambda x: -x[0]):
            t = (target-p)/s
            if t > cur:
                cur = t
                rst += 1
        return rst

        
if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                12,
                [10,8,0,5,3],
                [2,4,1,1,3]
            ),
            3
        ),
        (
            (
                10,
                [6,8],
                [3,2]
            ),
            2
        ),
    ]
    test(Solution().carFleet, test_data)

