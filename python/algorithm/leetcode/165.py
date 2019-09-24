class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        for n1, n2 in zip(v1, v2):
            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1
            else:
                continue
        l1 = len(v1)
        l2 = len(v2)
        if l1 > l2:
            if sum(v1[l2:]) > 0:
                return 1
        elif l1 < l2:
            if sum(v2[l1:]) > 0:
                return -1
        return 0


if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            (
                "1.0.1",
                "1"
            ),
            1
        ),
        (
            (
                "7.5.2.4",
                "7.5.3"
            ),
            -1
        ),
        (
            (
                "1.01",
                "1.001"
            ),
            0
        ),
        
        (
            (
                "1.0",
                "1.0.0"
            ),
            0
        )
    ]
    test(Solution().compareVersion, test_data)
