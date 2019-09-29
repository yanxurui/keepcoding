# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        return self.binary_search(target, array, 0,0, len(array)-1,len(array[0])-1)

    def binary_search(self, target, array, i1,j1, i2,j2):
        if i1 > i2 or j1 > j2:
            return False
        i3 = (i1 + i2)/2
        j3 = (j1 + j2)/2
        m = array[i3][j3]
        if target == m:
            return True
        elif target > m:
            return self.binary_search(target, array, i1,j3+1, i3,j2) or \
                   self.binary_search(target, array, i3+1,j1, i2,j2)
        else:
            return self.binary_search(target, array, i1,j1, i3-1,j2) or \
                   self.binary_search(target, array, i3,j1, i2,j3-1)


# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                1,
                [
                    [1,2,3],
                    [2,3,4]
                ]   
            ),
            True
        ),
        (
            (
                0,
                [
                    [1,2,3],
                    [2,3,4]
                ]   
            ),
            False
        ),
    ]
    test(Solution().Find, test_data)