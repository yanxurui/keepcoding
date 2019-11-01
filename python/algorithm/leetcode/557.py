class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([w[::-1] for w in s.split(' ')])

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            "Let's take LeetCode contest",
            "s'teL ekat edoCteeL tsetnoc"
        )
    ]
    test(Solution().reverseWords, test_data)

