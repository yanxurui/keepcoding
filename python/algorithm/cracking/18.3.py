# -*- coding:utf-8 -*-

class NextElement:
    def findNext(self, A, n):
        # write code here
        rst = []
        A_sorted = []
        for i in range(len(A)-1, -1, -1):
            j = self.bs(A_sorted, A[i])
            if j == len(A_sorted):
                rst.append(-1)
                A_sorted.append(A[i])
            else:
                rst.append(A_sorted[j])
                A_sorted.insert(j, A[i])
        return rst[::-1]


    def bs(self, nums, k):
        '''find the idx of the first ele that is greater than k'''
        l = 0
        h = len(nums)-1
        while l <= h:
            m = (l+h)//2
            if k < nums[m]:
                h = m-1
            else:
                l = m+1
        return l



if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [11,13,10,5,12,21,3],
                7
            ),
            [12,21,12,12,21,-1,-1]
        ),
        
    ]
    test(NextElement().findNext, test_data)
