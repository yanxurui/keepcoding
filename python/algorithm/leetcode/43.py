# https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        buf = [0] * (l1+l2)
        # num1[i] * num2[j] will be placed at [i+j, i+j+1]
        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                mul = int(num1[i])*int(num2[j])
                p1 = i + j
                p2 = p1 + 1
                s = buf[p2] + mul
                buf[p2] = s%10
                buf[p1] += s//10
        i = 0
        while i < len(buf)-1 and buf[i] == 0:
            i += 1
        return ''.join(map(str, buf[i:]))


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
