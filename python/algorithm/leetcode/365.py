class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z > x+y:
            return False
        if z == 0:
            return True
        if z % self.gcd(x, y) == 0:
            return True
        return False
    def gcd(self, a, b):
        while b:
            a, b = b, a%b
        return a

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                3,5,4
            ),
            True
        ),
        (
            (
                2,6,5
            ),
            False
        ),
        (
            (
                0,0,0
            ),
            True
        ),
        (
            (
                0,0,1
            ),
            False
        ),
    ]
    test(Solution().canMeasureWater, test_data)

