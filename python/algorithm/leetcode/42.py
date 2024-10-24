# https://leetcode.com/problems/trapping-rain-water/discuss/17357/Sharing-my-simple-c%2B%2B-code%3A-O(n)-time-O(1)-space

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1 # left, right
        ml, mr = 0, 0 # maxleft, maxright
        total = 0
        while l <= r:
            if height[l] < height[r]:
                if height[l] < ml:
                    # there is an implicit condition here:
                    # height[ml] < height[ml]
                    total += ml - height[l]
                else:
                    ml = height[l]
                l += 1
            else:
                if height[r] < mr:
                    total += mr - height[r]
                else:
                    mr = height[r]
                r -= 1
        return total


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [0,1,0,2,1,0,1,3,2,1,2,1],
            6
        )
    ]
    test(Solution().trap, test_data)
