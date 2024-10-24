from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        def bs1(arr, n):
            '''find the first index i where arr[i] > n'''
            l = 0
            r = len(arr)-1
            while l <= r:
                m = (l+r)//2
                if n >= arr[m]:
                    l = m + 1
                else:
                    r = m - 1
            return l

        def bs2(arr, n):
            '''find the first index i where arr[i] > n'''
            l = 0
            r = len(arr)-1
            while l <= r:
                m = (l+r)//2
                if n > arr[m]:
                    l = m + 1
                else:
                    r = m - 1
            return l

        start = sorted([a for a,b in flowers])
        end = sorted([b for a,b in flowers])
        ans = []
        for p in people:
            # how many flowers start bloom before p
            # how many flowers end bloom before p
            # the difference is how many flowers are blooming at p
            ans.append(bs1(start, p) - bs2(end, p))
        return ans


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [[1,6],[3,7],[9,12],[4,13]],
                [2,3,7,11]
            ),
            [1,2,2,2]
        ),
        (
            (
                [[1,10],[3,3]],
                [3,3,2]
            ),
            [2,2,1]
        )
    ]
    test(Solution().fullBloomFlowers, test_data)

