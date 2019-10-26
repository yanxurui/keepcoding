# -*- coding:utf-8 -*-
LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
THOUSANDS = ["", "Thousand", "Million", "Billion"]

class ToString:
    def toString(self, num):
        if num == 0:
            return 'Zero'
        buf = []
        for t in THOUSANDS:
            tmp = self.util(num%1000)
            if t and tmp:
                tmp.append(t)
            if tmp:
                buf.append(' '.join(tmp))
            num //= 1000
            if num == 0:
                break
        return ','.join(buf[::-1])

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


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            1234,
            "One Thousand,Two Hundred Thirty Four"
        ),
        (
            10**6,
            'One Million'
        ),
    ]
    test(ToString().toString, test_data)
