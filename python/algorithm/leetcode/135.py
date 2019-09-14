class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        C = [1] * n
        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                C[i] = C[i-1] + 1
        C = C[::-1]
        ratings = ratings[::-1]
        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                C[i] = max(C[i], C[i-1] + 1)
        return sum(C)
        
        
if __name__ == '__main__':
    from testfunc import test
    test_data = [  
        (
            ([1,0,2]),
            5
        ),
        (
            ([1,2,2]),
            4
        ),
        (
            ([1,2,87,87,87,2,1]),
            13
        ),
        (
            ([1,2,4,4,4,3]),
            10
        ),
        (
            ([1,3,4,5,2]),
            11
        )

    ]
    test(Solution().candy, test_data)
