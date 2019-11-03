from typing import List
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        rst = []
        for i in range(len(A), 1, -1):
            j = A.index(i)
            if j == i-1:
                continue
            if j != 0:
                self.reverse(A, 0, j)
                rst.append(j+1)
            self.reverse(A, 0, i-1)
            rst.append(i)
        return rst

    def reverse(self, nums, b, e):
        while b < e:
            tmp = nums[b]
            nums[b] = nums[e]
            nums[e] = tmp
            b += 1
            e -= 1

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [3,2,4,1],
            [3, 4, 2, 3, 2]
        ),
        (
            [1,2,3],
            []
        ),
    ]
    test(Solution().pancakeSort, test_data)

