class Solution(object):
    def dfs(self, ans, s, tmp):
        if len(s) == 0 and len(tmp) == 4:
            ans.append('.'.join(tmp))
            return
        if len(s) == 0 or len(tmp) == 4:
            return
        l = min(3, len(s))
        if s[0] == '0':
            l = 1
        for i in range(1, l+1):
            part = s[:i]
            if int(part) <= 255:
                tmp.append(part)
                self.dfs(ans, s[i:], tmp)
                tmp.pop()

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.dfs(ans, s, [])
        return ans


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            "25525511135",
            ["255.255.11.135", "255.255.111.35"]
        ),
        (
            "123",
            []
        )
    ]
    test(Solution().restoreIpAddresses, test_data)
