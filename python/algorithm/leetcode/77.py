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



if __name__ == '__main__':
    from testfunc import test

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
    test(Solution().combine, test_data)
