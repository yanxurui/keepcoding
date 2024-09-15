from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # todo

        
if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            [0,1,0],
            [0,0,1]
        ),
        (
            [5,2,3,1],
            [1,2,3,5]
        ),
        (
            [5,1,1,2,0,0],
            [0,0,1,1,2,5]
        )
    ]
    test(Solution().sortArray, test_data)
