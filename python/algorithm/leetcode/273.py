# https://leetcode.com/problems/integer-to-english-words/discuss/70625/My-clean-Java-solution-very-easy-to-understand
LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
THOUSANDS = ["", "Thousand", "Million", "Billion"]

class Solution:
    
    def util(self, num):
        if num == 0:
            return []
        elif num < 20:
            return [LESS_THAN_20[num]]
        elif num < 100:
            return [TENS[num//10]] + self.util(num%10)
        else:
            # 100<= num <1000
            return self.util(num//100) + ['Hundred'] + self.util(num%100)

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        buf = []
        for t in THOUSANDS:
            tmp = self.util(num%1000)
            if t and tmp:
                tmp.append(t)
            buf = tmp + buf
            num //= 1000
            if num == 0:
                break
        return ' '.join(buf)


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            123,
            "One Hundred Twenty Three"
        ),
        (
            12345,
            "Twelve Thousand Three Hundred Forty Five"
        ),
        (
            1234567,
            "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
        ),
        (
            1234567891,
            "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
        ),
        (
            20,
            "Twenty"
        ),
        (
            1000000,
            "One Million"
        )
    ]
    test(Solution().numberToWords, test_data)
