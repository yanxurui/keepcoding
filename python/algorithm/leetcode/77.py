# todo: mask is not needed

class Solution(object):
    def cb(self, ans, tmp, mask, k):
        if k == 0:
            ans.append(tmp)
            return
        if len(tmp) == 0:
            start = 0
        else:
            start = tmp[-1]
        for i in range(start, len(mask)):
            if mask[i] == 1:
                mask[i] = 0
                self.cb(ans, tmp+[i+1], mask, k-1)
                mask[i] = 1

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        mask = [1]*n
        ans = []
        self.cb(ans, [], mask, k)
        return ans


class Solution2(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        rst = []
        self.sub(rst, [], n, k, 1)
        return rst

    def sub(self, rst, tmp, n, k, i):
        if len(tmp) == k:
            rst.append(tmp)
            return
        if i > n:
            return
        self.sub(rst, tmp+[i], n, k, i+1)
        self.sub(rst, list(tmp), n, k, i+1)



# iteratively, very slow
class Solution3(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        rst = []
        tmp = [[]]
        for i in range(1, n+1):
            l = len(tmp)
            for j in range(l):
                t = tmp[j]
                s = t+[i]
                if len(s) == k:
                    rst.append(s)
                else:
                    tmp.append(s)
        return rst


# https://leetcode.com/problems/combinations/discuss/27024/1-liner-3-liner-4-liner
# recursively
class Solution4(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]
        rst = []
        for i in range(k, n+1):
            for r in self.combine(i-1, k-1):
                r.append(i)
                rst.append(r)
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            (4, 2),
            [
                [2,4],
                [3,4],
                [2,3],
                [1,2],
                [1,3],
                [1,4],
            ]
        )
    ]
    test(Solution4().combine, test_data, compare=unordered_equal)
