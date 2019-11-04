from typing import List
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        kinds = len(set(candies))
        if kinds > len(candies)//2:
            return len(candies)//2
        else:
            return kinds

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [1,1,2,2,3,3],
            3
        ),
        (
            [1,1,2,3],
            2
        ),
    ]
    test(Solution().distributeCandies, test_data)

