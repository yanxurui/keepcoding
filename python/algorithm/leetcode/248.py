from typing import List

class Solution:
    mapping = {
        "0":"0",
        "1":"1",
        "6":"9",
        "8":"8",
        "9":"6"
    }

    # @cache
    def countStrobogrammatic(self, n):
        if n == 1:
            return 3
        elif n == 2:
            return 4
        elif n == 3:
            return 12
        else:
            return 5*self.countStrobogrammatic(n-2)

    def recursive(self, cur, remain, ans):
        if remain == 0:
            if len(cur) == 1 or cur[0] != '0':
                ans.append(cur)
        else:
            for k,v in self.mapping.items():
                self.recursive(k+cur+v, remain-2, ans)

    def findStrobogrammatic(self, n: int) -> List[str]:
        ans = []
        if n % 2 == 1:
            for c in '018':
                self.recursive(c, n-1, ans)
        else:
            self.recursive('', n, ans)
        return ans
    
    def GE(self, num1, num2):
        assert len(num1) == len(num2)
        for c1,c2 in zip(num1, num2):
            if c1 > c2:
                return True
            elif c1 < c2:
                return False
        return True

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        ans = 0
        nlow = len(low)
        nhigh = len(high)
        if nlow == nhigh:
            for n in self.findStrobogrammatic(nlow):
                if self.GE(n, low) and self.GE(high, n):
                    ans += 1
        else:
            for n in self.findStrobogrammatic(nlow):
                if self.GE(n, low):
                    ans += 1
            for n in self.findStrobogrammatic(nhigh):
                if self.GE(high, n):
                    ans += 1
            for i in range(nlow+1, nhigh):
                ans += self.countStrobogrammatic(self, i)
        return ans


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            ('50', '100'),
            3
        ),
        (
            ('0', '0'),
            1
        ),
    ]
    test(Solution().strobogrammaticInRange, test_data)
