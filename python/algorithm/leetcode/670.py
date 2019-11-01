class Solution:
    def swap(self, num, i, j):
        tmp = num[i]
        num[i] = num[j]
        num[j] = tmp
    def max(self, num):
        # the maximum value to the right
        rst = [(0,0)] * len(num)
        for i in range(len(num)-1, -1, -1):
            if i == len(num)-1:
                rst[i] = (num[i], i)
            else:
                if num[i] > rst[i+1][0]: # > very important
                    rst[i] = (num[i], i)
                else:
                    rst[i] = rst[i+1]
        return rst
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        max_to_right = self.max(num)
        for i in range(len(num)):
            m, p = max_to_right[i]
            if p != i and m > num[i]:
                # m might be equal to num[i]
                self.swap(num, i, p)
                break
        return int(''.join(num))


# https://leetcode.com/problems/maximum-swap/discuss/107068/Java-simple-solution-O(n)-time
class Solution2:
    def maximumSwap(self, num: int) -> int:
        digits = list(map(int, str(num)))
        pos = {}
        for i, d in enumerate(digits):
            pos[d] = i
        for i in range(len(digits)):
            for d in range(9, digits[i], -1):
                j = pos.get(d)
                if j is not None and j > i:
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(map(str, digits)))
        return num


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            2736,
            7236
        ),
        (
            9973,
            9973
        ),
        (
            1993,
            9913
        ),
        (
            98368,
            98863
        ),
    ]
    test(Solution2().maximumSwap, test_data)

