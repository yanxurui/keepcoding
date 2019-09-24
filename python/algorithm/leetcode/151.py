class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([x for x in s.split(' ')[::-1] if x])


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            ('the sky is blue'),
            'blue is sky the'
        ),
        (
            ("  hello world!  "),
            "world! hello"
        ),
        (
            ("a good   example"),
            "example good a"
        ),
        (
            (''),
            ''
        )
    ]
    test(Solution().reverseWords, test_data)

