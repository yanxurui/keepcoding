from collections import defaultdict

class Solution(object):
    def count(self, seq):
        i = 0
        n = len(seq)
        out = []
        while i < n:
            count = 1
            j = i+1
            while j < n and seq[j] == seq[i]:
                count += 1
                j += 1
            out.append(count)
            out.append(seq[i])
            i = j
        return ''.join(map(str, out))

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        out = '1'
        for i in range(n-1):
            out = self.count(out)
        return out

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            1,
            '1'
        ),
        (
            4,
            '1211'
        )
    ]
    test(Solution().countAndSay, test_data)
