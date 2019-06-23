class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if len(s) == 0:
            return False

        exp = False
        point = False
        digit = False
        prev = None

        for c in s:
            if c == '-' or c == '+':
                # sign can be right after e
                # sign must be at the beginning of the string
                if not (prev is None or prev == 'e'):
                    return False
            elif c == 'e':
                if not digit:
                    # e must be following a digit
                    return False
                if exp:
                    # e can only exist once
                    return False
                exp = True
            elif c == '.':
                # if not (prev and prev.isdigit()):
                #     return False
                if exp:
                    return False
                if point:
                    return False
                point = True
            elif c.isdigit():
                digit = True
            else:
                return False
            prev = c

        if not digit:
            return False
        if prev == 'e' or prev == '+' or prev == '-':
            return False
        return True


        
        
if __name__ == '__main__':
    from testfunc import test

    test_data = [
        ("0", True),
        (" 0.1 ", True),
        ("abc", False),
        ("1 a", False),
        ("2e10", True),
        (" -90e3   ", True),
        (" 1e", False),
        ("e3", False),
        (" 6e-1", True),
        (" 99e2.5 ", False),
        ("53.5e93", True),
        (" --6 ", False),
        ("-+3", False),
        ("95a54e53", False),
        ("12-45", False),
        ("1.1.1", False),
        ("1.", True),
        (".1", True),
        ("1e1e1", False),
        (".", False),
        ("4e+", False),
        ("46.e3", True),
    ]
    test(Solution().isNumber, test_data)
