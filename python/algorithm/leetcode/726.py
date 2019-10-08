# https://leetcode.com/problems/number-of-atoms/discuss/140802/Python-20-lines-very-readable-simplest-and-shortest-solution-36-ms-beats-100

from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        dic = defaultdict(int)
        stack = []
        ele = ''
        cnt = ''
        coef = 1
        for c in formula[::-1]:
            if c.isdigit():
                cnt += c
            elif c.isupper():
                cnt = int(cnt[::-1]) if cnt else 1
                ele += c
                dic[ele[::-1]] += cnt * coef
                ele = ''
                cnt = ''
            elif c.islower():
                ele += c
            elif c == ')':
                cnt = int(cnt[::-1])
                stack.append(cnt)
                coef *= cnt
                cnt = ''
            elif c == '(':
                coef //= stack.pop()
            else:
                assert False, 'wrong input'
        return ''.join(['%s%d'%(k, v) if v > 1 else k for k,v in sorted(dic.items(), key=lambda item:item[0])])


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ('H2O'),
            'H2O'
        ),
        (
            ('Mg(OH)2'),
            'H2MgO2'
        ),
        (
            ('K4(ON(SO3)2)2'),
            'K4N2O14S4'
        ),
        (
            ("Be32"),
            "Be32"
        )
    ]
    test(Solution().countOfAtoms, test_data)
