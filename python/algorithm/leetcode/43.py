class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if len(num1) > len(num2):
            tmp = num1
            num1 = num2
            num2 = tmp
        N1, N2 = [], []
        for d1 in num1[::-1]:
            N1.append(int(d1))
        for d2 in num2[::-1]:
            N2.append(int(d2))
        T = []

        for d1 in N1:
            t = []
            c = 0
            for d2 in N2:
                tmp = d1*d2+c
                t.append(tmp%10)
                c = tmp/10
            if c > 0:
                t.append(c)
            T.append(t)

        # import pdb
        # pdb.set_trace()
        prod = []
        c = 0
        left = 0
        for i in range(len(T)+len(T[-1])-1):
            tmp = c
            for j in range(left, min(i+1, len(T))):
                if len(T[j])+j > i:
                    tmp += T[j][i-j]
                else:
                    left = j+1
            prod.append(tmp%10)
            c = tmp / 10
        if c > 0:
            prod.append(c)

        # remove leading 0
        prod = prod[::-1]
        s = 0
        while s < len(prod)-1 and prod[s] == 0:
            s += 1
        prod = prod[s:]
        return ''.join(map(str, prod))


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ("2", "3"),
            "6"
        ),
        (
            ("123", "456"),
            "56088"
        ),
        (
            ("9133", "0"),
            "0"
        ),
        (
            ("408", "5"),
            "2040"
        )
    ]
    test(Solution().multiply, test_data)
