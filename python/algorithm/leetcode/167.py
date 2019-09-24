class Solution:
    def bs(self, nums, l, h, t):
        if l > h:
            return None
        m = (l + h)//2
        if nums[m] == t:
            return m
        if nums[m] < t:
            return self.bs(nums, m+1, h, t)
        if nums[m] > t:
            return self.bs(nums, l, m-1, t)

    def twoSum(self, numbers, target: int):
        for i in range(len(numbers)):
            t = target - numbers[i]
            if t >= numbers[i]:
                i2 = self.bs(numbers, i+1, len(numbers)-1, t)
                if i2:
                    return [i+1, i2+1]


if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            (
                [2,7,11,15],
                9
            ),
            [1,2]
        ),
        (
            (
                [-1,0],
                -1
            ),
            [1,2]
        ),
        (
            (
                [0,0,3,4],
                0
            ),
            [1,2]
        )
    ]
    test(Solution().twoSum, test_data)
