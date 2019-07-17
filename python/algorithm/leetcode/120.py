class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        line = triangle[0]
        for i in range(1, len(triangle)):
            cur = []
            for j in range(i+1):
                v = triangle[i][j]
                if j == 0:
                    cur.append(v + line[0])
                elif j == i:
                    cur.append(v + line[j-1])
                else:
                    cur.append(v + min(line[j-1], line[j]))
            line = cur
        return min(line)
        
        
if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [
                 [2],
                [3,4],
               [6,5,7],
              [4,1,8,3]
            ],
            11
        ),
    ]
    test(Solution().minimumTotal, test_data)
