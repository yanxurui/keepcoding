# https://leetcode.com/problems/partition-labels/discuss/113293/C%2B%2B-6-lines-O(n)-or-O(1)-two-simple-passes

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return [0]
        pos = {}
        for i, c in enumerate(S):
            pos[c] = i
        idx = last_i = 0
        rst = []
        for i, c in enumerate(S):
            idx = max(idx, pos[c])
            if i == idx:
                rst.append(i - last_i + 1)
                last_i = i + 1
        return rst
        
        
if __name__ == '__main__':
    from testfunc import test
    test_data = [  
        (
            ('ababcbacadefegdehijhklij'),
            [9,7,8]
        ),
        (
            ('a'),
            [1]
        ),
        (
            (''),
            [0]
        ),
    ]
    test(Solution().partitionLabels, test_data)
