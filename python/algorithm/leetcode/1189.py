class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {c: 0 for c in 'balon'}
        for c in text:
            if c in d:
                d[c] += 1
        d['l'] = d['l']//2
        d['o'] = d['o']//2
        return min(d.values())


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            'nlaebolko',
            1
        ),
        (
            'loonbalxballpoon',
            2
        ),
        (
            'leetcode',
            0
        )
    ]
    test(Solution().maxNumberOfBalloons, test_data)

