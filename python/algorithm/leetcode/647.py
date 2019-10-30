class Solution:
    def countSubstrings(self, s: str) -> int:
        rst = 0
        for i in range(len(s)):
            rst += self.sub(s, i)
        return rst

    def sub(self, s, i):
        # compute number of palindromic strings that are symetric to s[i] or (s[i], s[i+1])
        rst = 0
        l = i - 1
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        rst += i - l

        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        rst += i - l
        return rst




if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            'abc',
            3
        ),
        (
            'aaa',
            6
        ),
    ]
    test(Solution().countSubstrings, test_data)

