import os
from collections import defaultdict

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for p in paths:
            parts = p.split(' ')
            directory = parts[0]
            for i in range(1, len(parts)):
                j = parts[i].find('(')
                name = parts[i][:j]
                content = parts[i][j+1:-1]
                d[content].append(os.path.join(directory, name))
        rst = []
        for content, paths in d.items():
            if len(paths) > 1:
                rst.append(paths)
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import nested_unordered_equal
    test_data = [  
        (
            [
                "root/a 1.txt(abcd) 2.txt(efgh)",
                "root/c 3.txt(abcd)",
                "root/c/d 4.txt(efgh)",
                "root 4.txt(efgh)"
            ],
            [
                [
                    "root/a/2.txt",
                    "root/c/d/4.txt",
                    "root/4.txt"
                ],
                [
                    "root/a/1.txt",
                    "root/c/3.txt"
                ]
            ]
        )
    ]
    test(Solution().findDuplicate, test_data, compare=nested_unordered_equal)

