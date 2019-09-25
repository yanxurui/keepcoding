# https://leetcode.com/problems/largest-number/discuss/53157/A-simple-C%2B%2B-solution

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums) -> str: 
        tmp = map(str, nums)
        tmp = sorted(tmp, key=cmp_to_key(lambda a,b: -1 if (a+b)<(b+a) else 1))
        res = ''.join(tmp[::-1])
        for i in range(len(res)):
            if res[i] != '0':
                break
        return res[i:]


if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            ([10,2]),
            '210'
        ),
        (
            ([3,30,34,5,9]),
            '9534330'
        ),
        (
            ([76,765,6]),
            '767656'
        ),
        (
            ([76,765,4]),
            '767654'
        ),
        (
            ([0,0,0]),
            '0'
        )
    ]
    test(Solution().largestNumber, test_data)
