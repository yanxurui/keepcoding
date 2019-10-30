from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        stack = [(sr, sc)]
        oldColor = image[sr][sc]
        while stack:
            cr, cc = stack.pop()
            if image[cr][cc] != newColor:
                # not visited
                image[cr][cc] = newColor
                for x, y in [(cr-1, cc), (cr+1, cc), (cr, cc-1), (cr, cc+1)]:
                    if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == oldColor:
                        stack.append((x, y))
        return image


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [[1,1,1],[1,1,0],[1,0,1]],
                1, 1, 2
            ),
            [[2,2,2],[2,2,0],[2,0,1]]
        ),
        (
            (
                [[0,0,0],[0,0,0]],
                0, 0, 2
            ),
            [[2,2,2],[2,2,2]]
        ),
    ]
    test(Solution().floodFill, test_data)

