# -*- coding:utf-8 -*-
class TwoStacks:
    def twoStacksSort(self, numbers):
        # write code here
        stack = []
        def recursive(nums, k):
            if k <= 1:
                return
            recursive(nums, k-1)
            for i in range(k-1):
                stack.append(nums.pop(0))
            target = nums.pop(0)
            done = False
            while stack:
                k = stack.pop()
                if not done and k > target:
                    nums.insert(0, target)
                    done = True
                nums.insert(0, k)
            assert not stack
            if not done:
                nums.insert(0, target)
        recursive(numbers, len(numbers))
        return numbers


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            ([1,2,3,4,5]),
            [5,4,3,2,1]
        )
    ]
    test(TwoStacks().twoStacksSort, test_data)

