class Solution:
    def findRepeatedDnaSequences(self, s: str):
        seen = set()
        res = set()
        for i in range(len(s)-9):
            sub = s[i:i+10]
            if sub in seen:
                res.add(sub)
            else:
                seen.add(sub)
        return list(res)


if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            ('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'),
            ["AAAAACCCCC", "CCCCCAAAAA"]
        ),
        (
            ("AAAAAAAAAAA"),
            ["AAAAAAAAAA"]
        )
    ]
    test(Solution().findRepeatedDnaSequences, test_data)
