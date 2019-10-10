# -*- coding:utf-8 -*-
class ReverseEqual:
    def checkReverseEqual(self, s1, s2):
        # write code here
        return self.kmp(s1*2, s2)
    def kmp(self, s, pat):
        def kmp_lps(pat):
            lps = [0]
            prev = 0
            for i in range(1, len(pat)):
                while prev and pat[i] != pat[prev]:
                    prev = lps[prev-1]
                if pat[i] == pat[prev]:
                    prev += 1
                lps.append(prev)
            return lps
        lps = kmp_lps(pat)
        i = 0
        for c in s:
            if pat[i] == c:
                i += 1
                if i == len(pat):
                    return True
            else:
                i = lps[max(0,i-1)]
        return False


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                "Hello world",
                "worldhello "
            ),
            False
        ),
        (
            (
                "waterbottle",
                "erbottlewat"
            ),
            True
        )
    ]
    test(ReverseEqual().checkReverseEqual, test_data)
    test_data = [
        (
            (
                "Hello world",
                "world"
            ),
            True
        ),
        (
            (
                "aaaaabaaaaa",
                "aaabaaa"
            ),
            True
        )
    ]
    test(ReverseEqual().kmp, test_data)

