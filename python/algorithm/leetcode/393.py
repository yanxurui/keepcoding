class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        
        i = 0
        while i < len(data):
            num_bytes = 0
            mask = 1<<7
            while mask & data[i]:
                num_bytes += 1
                mask = mask >> 1
            i += 1
            if num_bytes:
                if num_bytes < 2 or num_bytes > 4:
                    return False
                else:
                    for _ in range(1, num_bytes): # n-1
                        if i >= len(data): # check
                            return False
                        if not ((data[i] & 1<<7) and not (data[i] & 1<<6)):
                            return False
                        i += 1
        return True



if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [197, 130, 1],
            True
        ),
        (
            [235, 140, 4],
            False
        ),
        (
            [248,130,130,130],
            False
        ),
        (
            [250,145,145,145,145],
            False
        )
    ]
    test(Solution().validUtf8, test_data)
