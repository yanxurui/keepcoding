# -*- coding:utf-8 -*-

class Change:
    def countChanges(self, dic, n, s, t):
        # write code here
        wordSet = set(dic)
        layer = set([s])
        n = 0
        while layer:
            newLayer = set()
            for w in layer:
                if w == t:
                    return n
                for i in range(len(w)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        neww = w[:i]+c+w[i+1:]
                        if neww in wordSet:
                            newLayer.add(neww)
            wordSet -= newLayer
            layer = newLayer
            n += 1
        return -1


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode, ListNode
    test_data = [
        (
            (
                ["abc","adc","bdc","aaa"],4,"abc","bdc"
            ),
            2
        )
    ]
    test(Change().countChanges, test_data)
