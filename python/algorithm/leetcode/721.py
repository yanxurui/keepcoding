from typing import List
from collections import defaultdict
class UnionFind:
    def __init__(self):
        self.d = {}
    def union(self, x, y):
        p1 = self.find(x)
        p2 = self.find(y)
        if p1 == p2:
            return
        self.d[p1] = p2

    def find(self, x):
        y = self.d.get(x, None)
        if y is None or y == x:
            return x
        else:
            return self.find(y)

class Solution:
    def merge(self, a1, a2):
        assert a1[0] == a2[0]

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        rst = []
        owner = {}
        uf = UnionFind()
        rst = []
        for i in range(len(accounts)):
            if len(accounts[i]) == 1:
                rst.append(accounts[i])
            else:
                parent = accounts[i][1]
                for j in range(2, len(accounts[i])):
                    uf.union(accounts[i][j], parent)
        emails = defaultdict(set)
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                name = accounts[i][0]
                e = accounts[i][j]
                owner[e] = name
                emails[uf.find(e)].add(e)
        for parent, all_emails in emails.items():
            a = sorted(list(all_emails))
            a.insert(0, owner[parent])
            rst.append(a)
        return rst



if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]],
            [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
        )
    ]
    test(Solution().accountsMerge, test_data, compare=unordered_equal)

