from typing import List

class Solution:
    mapping = {
        "0":"0",
        "1":"1",
        "6":"9",
        "8":"8",
        "9":"6"
    }

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


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            2,
            ["11","69","88","96"]
        ),
        (
            1,
            ["0","1","8"]
        ),
    ]
    test(Solution().findStrobogrammatic, test_data)
