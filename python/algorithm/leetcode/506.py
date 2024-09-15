from typing import List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = [(i,s) for i,s in enumerate(score)]
        ranks.sort(key=lambda item: -item[1])
        ans = ['',] * len(score)
        for j,(i,s) in enumerate(ranks):
            if j == 0:
                ans[i] = "Gold Medal"
            elif j == 1:
                ans[i] = "Silver Medal"
            elif j == 2:
                ans[i] = "Bronze Medal"
            else:
                ans[i] = str(j+1)
        return ans


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [5,4,3,2,1],
            ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
        ),
        (
            [10,3,8,9,4],
            ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
        )
    ]
    test(Solution().findRelativeRanks, test_data)

