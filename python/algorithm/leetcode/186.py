from typing import List

# https://leetcode.com/problems/reverse-words-in-a-string-ii/solutions/53832/python-solution/
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # 1. reverse each word
        # ["e","h","t"," ","y","k","s"," ","s","i"," ","e","u","l","b"],
        b = 0
        for i in range(len(s)):
            if s[i] == ' ':
                self.reverse(s, b, i-1)
                b = i + 1
            elif i == len(s) - 1:
                self.reverse(s, b, i)

        # 2. reverse the entire string
        # ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
        self.reverse(s, 0, len(s)-1)
        return s

    def reverse(self, s, b, e):
        while b < e:
            s[b], s[e] = s[e], s[b]
            b += 1
            e -= 1



if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"],
            ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
        ),
        (
            ["a"],
            ["a"]
        )
    ]
    test(Solution().reverseWords, test_data)
