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

        
if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [2,3,1,1,4],
            2
        )
    ]
    test(Solution().jump, test_data)

