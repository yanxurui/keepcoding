class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        buf = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 10 * num + int(s[i])
            elif s[i] == '[':
                t = 1
                for j in range(i+1, len(s)):
                    if s[j] == '[':
                        t += 1
                    elif s[j] == ']':
                        t -= 1
                        if t == 0:
                            break
                buf.append(self.decodeString(s[i+1:j])*num)
                num = 0
                i = j
            else:
                buf.append(s[i])
            i += 1
        return ''.join(buf)


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ('3[a]2[bc]'),
            'aaabcbc'
        ),
        (
            ('3[a2[c]]'),
            'accaccacc'
        ),
        (
            ('2[abc]3[cd]ef'),
            'abcabccdcdcdef'
        )
    ]
    test(Solution().decodeString, test_data)
