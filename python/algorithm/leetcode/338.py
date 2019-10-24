from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        rst = [0] * (num+1)
        rst[1] = 1
        i = 1
        while i < num:
            for j in range(1, i):
                rst[i+j] = rst[i]+rst[j]
                if i+j >= num:
                    return rst
            rst[2*i] = rst[i]
            i *= 2
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            0,
            [0]
        ),
        (
            2,
            [0,1,1]
        ),
        (
            5,
            [0,1,1,2,1,2]
        )
    ]
    test(Solution().countBits, test_data)
