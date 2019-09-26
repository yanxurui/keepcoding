class Solution:
    def maxProfit(self, k, prices) -> int:
        # interval
        tmp = []
        l = len(prices)
        if l < 2:
            return 0
        for i in range(1, l):
            tmp.append(prices[i] - prices[i-1])

        # merge
        tmp2 = []
        pos = tmp[0] > 0
        prev = tmp[0]
        for i in tmp[1:]:
            if pos:
                if i >= 0:
                    prev += i
                else:
                    tmp2.append(prev)
                    pos = False
                    prev = i
            else:
                if i <= 0:
                    prev += i
                else:
                    tmp2.append(prev)
                    pos = True
                    prev = i
        tmp2.append(prev)
        # sort
        tmp3 = sorted(tmp2)[::-1]
        res = 0
        for i in range(min(len(tmp3), k)):
            if tmp3[i] <= 0:
                break
            res += tmp3[i]
        return res



if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            (
                2,
                [2,4,1]
            ),
            2
        ),
        (
            (
                2,
                [3,2,6,5,0,3]
            ),
            7
        ),
        (
            (
                1,
                [6,1,6,4,3,0,2]
            ),
            5
        ),
        (
            (
                2,
                [1,2,4]
            ),
            3
        ),
        (
            (
                2,
                [1,2,4,2,5,7,2,4,9,0]
            ),
            13
        )
    ]
    test(Solution().maxProfit, test_data)
