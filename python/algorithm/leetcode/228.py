class Solution:
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []
        left = nums[0]
        right = nums[0]
        rst = []
        for n in nums[1:]+[nums[-1]]:            
            if n - right == 1:
                right = n
            else:
                if left == right:
                    rst.append('%d'%left)
                else:
                    rst.append('%d->%d'%(left, right))
                left = n
                right = n
        return rst


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ([0,1,2,4,5,7]),
            ["0->2","4->5","7"]
        ),
        (
            ([0,2,3,4,6,8,9]),
            ["0","2->4","6","8->9"]
        )
    ]
    test(Solution().summaryRanges, test_data)
