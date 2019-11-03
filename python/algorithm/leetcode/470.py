# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

import random

def rand7():
    return random.randint(1, 7)

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        rst = self.rand49()
        if rst > 40:
            return self.rand10()
        else:
            return rst % 10 + 1

    def rand49(self):
        return 7 * (rand7()-1) + rand7()




if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [2, 7, 11, 15],
                9
            ),
            [0, 1]
        )
    ]
    test(Solution().twoSum, test_data)

