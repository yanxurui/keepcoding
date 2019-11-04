# https://leetcode.com/problems/day-of-the-week/discuss/382150/Python3-Solution-With-No-Knowledge-(Without-knowing-formulas-or-week-day-of-111971-beforehand)

days_in_each_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
class Solution:
    def hasLeap(self, year):
        if year % 4 == 0 and (year % 100 !=0 or year % 400 == 0):
            return 1
        else:
            return 0
    def daysSince(self, day, month, year):
        # number of days since 1970.12.31
        rst = 0
        for y in range(year-1, 1970, -1):
            rst += 365 + self.hasLeap(y)
        rst += sum(days_in_each_month[:month])
        if month > 2:
            rst += self.hasLeap(year)
        rst += day
        return rst
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # I know that
        # 2019.11.04
        # Monday
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        known = self.daysSince(4,11,2019)
        target = self.daysSince(day, month, year)
        return days[(target-known)%7]


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                31,
                8,
                2019
            ),
            'Saturday'
        ),
        (
            (
                18,
                7,
                1999
            ),
            'Sunday'
        ),
        (
            (
                15,
                8,
                1993
            ),
            'Sunday'
        ),
    ]
    test(Solution().dayOfTheWeek, test_data)

