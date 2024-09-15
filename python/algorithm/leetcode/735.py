class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        rst = []
        for a in asteroids:
            rst.append(a)
            self.explode(rst)

        return rst

    def explode(self, stack):
        while len(stack) >= 2:
            if stack[-2] > 0 and stack[-1] < 0:
                # will collide
                r = stack.pop()
                l = stack.pop()
                if l > -r:
                    # r exploded
                    stack.append(l)
                    break
                elif l < -r:
                    # l exploded
                    stack.append(r)
                else:
                    # both exploded
                    break
            else:
                break

if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [  
        (
            [5,10,-5],
            [5,10],
        ),
        (
            [8,-8],
            [],
        ),
        (
            [10,2,-5],
            [10]
        ),
        (
            [-2,-1,1,2],
            [-2,-1,1,2]
        )
    ]
    test(Solution().asteroidCollision, test_data)
