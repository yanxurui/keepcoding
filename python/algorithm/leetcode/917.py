class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        i, j = 0, len(S) - 1
        buf = list(S)
        while True:
            while i < j and not S[i].isalpha():
                i += 1
            while i < j and not S[j].isalpha():
                j -= 1
            if i >= j:
                break
            # swap
            buf[i], buf[j] = buf[j], buf[i]
            i += 1
            j -= 1
        return ''.join(buf)


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            'ab-cd',
            "dc-ba"
        ),
        (
            'a-bC-dEf-ghIj',
            "j-Ih-gfE-dCba"
        ),
        (
            'Test1ng-Leet=code-Q!',
            "Qedo1ct-eeLg=ntse-T!"
        ),
    ]
    test(Solution().reverseOnlyLetters, test_data)

