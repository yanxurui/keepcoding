class Solution:
    def partitionString(self, s: str) -> int:
        tmp = set()
        ans = 1
        for c in s:
            if c in tmp:
                ans += 1
                tmp = set()
            tmp.add(c)
        return ans

        
if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            'abacaba',
            4
        ),
        (
            'ssssss',
            6
        )
    ]
    test(Solution().partitionString, test_data)
