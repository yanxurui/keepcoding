# https://leetcode.com/problems/add-digits/discuss/68580/Accepted-C%2B%2B-O(1)-time-O(1)-space-1-Line-Solution-with-Detail-Explanations

# input: 1,2,3,4,5,6,7,8,9,10,11,12,13,14...
# output:1,2,3,4,5,6,7,8,9. 1, 2, 3, 4, 5...
class Solution:
    def addDigits(self, num: int) -> int:
        return (num-1) % 9 + 1 if num else 0


if __name__ == '__main__':
    from testfunc import test
    test_data = [  
        (
            38,
            2
        ),
        (
            0,
            0
        ),
    ]
    test(Solution().addDigits, test_data)
