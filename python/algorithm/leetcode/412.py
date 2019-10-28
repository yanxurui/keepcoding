# https://leetcode.com/problems/fizz-buzz/discuss/89931/Java-4ms-solution-Not-using-%22%22-operation

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rst = list(map(str, range(1, n+1)))
        Fizz, Buzz = 0, 0
        for i in range(n):
            Fizz += 1
            Buzz += 1
            if Fizz == 3 and Buzz == 5:
                rst[i] = 'FizzBuzz'
                Fizz = 0
                Buzz = 0
            elif Fizz == 3:
                rst[i] = 'Fizz'
                Fizz = 0
            elif Buzz == 5:
                rst[i] = 'Buzz'
                Buzz = 0

        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            15,
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz"
            ]
        )
    ]
    test(Solution().fizzBuzz, test_data)

