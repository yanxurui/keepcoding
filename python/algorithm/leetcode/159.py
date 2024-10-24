from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res = 0
        d = {}
        i, j = 0, 0
        while i < len(s) and j < len(s)+1:
            if j == len(s):
                res = max(res, j-i)
                break
            c = s[j]
            if s[j] not in d and len(d) == 2:
                # found the max substring starting from i and ends at j-1
                res = max(res, j-i)

                # find which char to remove
                m_k, m_v = None, None
                for k, v in d.items():
                    if m_v is None or v < m_v:
                        m_k = k
                        m_v = v
                i = m_v + 1
                # remove a char
                del d[m_k]
            d[c] = j # record the last position of c
            j += 1
        return res


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            'eceba',
            3
        ),
        (
            'ccaabbb',
            5
        )
    ]
    test(Solution().lengthOfLongestSubstringTwoDistinct, test_data)

