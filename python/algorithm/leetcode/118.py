class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            line = []
            for j in range(i+1):
                if j == 0 or j == i:
                    line.append(1)
                else:
                    line.append(res[-1][j-1]+res[-1][j])
            res.append(line)
        return res

        
if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            5,
            [
                 [1],
                [1,1],
               [1,2,1],
              [1,3,3,1],
             [1,4,6,4,1]
            ]
        ),
    ]
    test(Solution().generate, test_data)
