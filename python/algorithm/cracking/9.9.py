# -*- coding:utf-8 -*-
class Queens:
    def dfs(self, n, cols, xy_diff, xy_sum):
        x = len(cols)
        if x == n:
            self.rst += 1
        else:
            for y in range(n):
                if y not in cols and (x-y) not in xy_diff and (x+y) not in xy_sum:
                    cols.add(y)
                    xy_diff.add(x-y)
                    xy_sum.add(x+y)
                    self.dfs(n, cols, xy_diff, xy_sum)
                    cols.remove(y)
                    xy_diff.remove(x-y)
                    xy_sum.remove(x+y)

    def nQueens(self, n):
        self.rst = 0
        self.dfs(n, set(), set(), set())
        return self.rst



# -*- coding:utf-8 -*-
class Queens2:
    def nQueens(self, n):
        # write code here
        self.rst = 0
        self.util(n, [0]*n, 0)
        return self.rst

    def util(self, n, cols, x):
        if x == n:
            self.rst += 1
        else:
            for y in range(n):
                cols[x] = y
                if self.place(cols, x):
                    self.util(n, cols, x+1)

    def place(self, cols, x):
        for i in range(x):
            if cols[i] == cols[x] or cols[i]-cols[x] == i-x or cols[i]+i == cols[x]+x:
                return False
        return True


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            1,
            1
        ),
        (
            2,
            0
        ),
        (
            3,
            0
        ),
        (
            12,
            14200
        ),
    ]
    # test(Queens().nQueens, test_data)
    test(Queens2().nQueens, test_data)
