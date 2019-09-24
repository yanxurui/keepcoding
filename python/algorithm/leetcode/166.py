# https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/51106/My-clean-Java-solution

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        buf = []
        buf.append('-' if numerator * denominator < 0 else '')
        numerator = abs(numerator)
        denominator = abs(denominator)
        buf.append(str(numerator // denominator))
        numerator %= denominator
        if numerator == 0:
            return ''.join(buf)
        buf.append('.')
        rec = {}
        rec[numerator] = len(buf)
        while numerator:
            numerator *= 10
            buf.append(str(numerator // denominator))
            numerator %= denominator
            if numerator in rec:
                buf.insert(rec.get(numerator), '(')
                buf.append(')')
                break
            rec[numerator] = len(buf)
        return ''.join(buf)


if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            (
                1, 2
            ),
            '0.5'
        ),
        (
            (
                2, 1
            ),
            '2'
        ),
        (
            (
                2, 3
            ),
            '0.(6)'
        ),
        (
            (
                -50, 8
            ),
            "-6.25"
        )
    ]
    test(Solution().fractionToDecimal, test_data)
