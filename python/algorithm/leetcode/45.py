class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = len(nums) - 1
        chains = [i]
        j = i - 1
        # in reverse order
        while j >= 0:
            if nums[j] >= i - j: # jump from j to i
                while len(chains) > 1 and nums[j] >= chains[-2]-j:
                    # if it's possible to jump from j to the position after i
                    chains.pop()
                chains.append(j)
                i = j
            j -= 1
        return len(chains) - 1


class Solution2(object):
    def jump(self, nums):
        rst = 0
        i = 0
        reach = 0
        destination = len(nums)-1
        while reach < destination:
            tmp = reach
            reach = max([j+nums[j] for j in range(i, reach+1)])
            i = tmp + 1
            rst += 1
        return rst


        
if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [2,3,1,1,4],
            2
        ),
        (
            [2],
            0
        ),
        (
            [1,2,0,0],
            2
        ),
    ]
    test(Solution2().jump, test_data)

