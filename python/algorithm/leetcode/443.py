from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        def fill(arr, i, s):
            for c in s:
                arr[i] = c
                i += 1
            return i
        i = j = k = 0
        while j < len(chars):
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            n = j - i
            chars[k] = chars[i]
            k += 1
            if n > 1:
                k = fill(chars, k, str(n))
            i = j
        return k


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            ["a","a","b","b","c","c","c"],
            6
        ),
        (
            ["a"],
            1
        ),
        (
            ["a","b","b","b","b","b","b","b","b","b","b","b","b"],
            4
        ),
    ]
    test(Solution2().compress, test_data)

