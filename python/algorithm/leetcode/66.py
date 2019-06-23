class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    break
            else:
                digits[i] = digits[i]+1
                break
        return digits
        
        
        
if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            [1,2,3],
            [1,2,4]
        ),
        (
            [4,3,2,1],
            [4,3,2,2]
        ),
        (
            [9],
            [1,0]
        )

    ]
    test(Solution().plusOne, test_data)
