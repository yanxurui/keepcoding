from collections import defaultdict, Counter

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        assert len(A) == len(B)
        n = len(A)
        dA = Counter(A)
        dB = Counter(B)
        d = defaultdict(int)
        for i in range(n):
            d[A[i]] += 1
            if A[i] != B[i]:
                d[B[i]] += 1
        candidates = set()
        for a, cnt in d.items():
            if cnt == n:
                candidates.add(a)
        if not candidates:
            return -1
        return min([n-max(dA[a], dB[a]) for a in candidates])


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [2,1,2,4,2,2],
                [5,2,6,2,3,2]
            ),
            2
        ),
        (
            (
                [3,5,1,2,3],
                [3,6,3,3,4]
            ),
            -1
        ),
    ]
    test(Solution().minDominoRotations, test_data)

