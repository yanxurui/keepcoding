from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        an = 0
        dp = [set()]
        for i, s in enumerate(arr):
            ss = set(s)
            if len(ss) < len(s):
                continue
            l = len(dp)
            for j in range(l):
                c = dp[j]
                if ss & c:
                    continue
                dp.append(ss | c)
        return max(len(s) for s in dp)

class Solution2:
    def maxLength(self, arr: List[str]) -> int:
        return self.recursive(arr, 0, '')

    def recursive(self, arr, i, tmp):
        if len(set(tmp)) != len(tmp):
            return 0
        if i >= len(arr):
            return len(tmp)
        return max(
            self.recursive(arr, i+1, tmp + arr[i]),
            self.recursive(arr, i+1, tmp))


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            ["un","iq","ue"],
            4
        ),
        (
            ["cha","r","act","ers"],
            6
        ),
        (
            ["abcdefghijklmnopqrstuvwxyz"],
            26
        ),
        (
            ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"],
            16
        ),
        (
            ['a', 'b', 'c', 'bef'],
            5
        )
    ]
    test(Solution().maxLength, test_data)

