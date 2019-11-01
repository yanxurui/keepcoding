digits = set(map(str, range(10)))
alphanum = set('abcdef') | digits

class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self.IPv4(IP):
            return 'IPv4'
        if self.IPv6(IP):
            return 'IPv6'
        return 'Neither'
        
    def IPv4(self, IP):
        parts = IP.split('.')
        if len(parts) != 4:
            return False
        for p in parts:
            if not (0 < len(p) <= 3):
                return False
            if (set(p)-digits):
                # contain non-digit
                return False
            if not (0<=int(p)<=255):
                return False
            if len(p) > 1 and p[0] == '0':
                # leading zero
                return False
        return True

    def IPv6(self, IP):
        parts = IP.split(':')
        if len(parts) != 8:
            return False
        if len(parts[0]) > 1 and parts[0][0] == '0':
            # leading zero
            return False
        for p in parts:
            if not (0 < len(p) <= 4):
                return False
            p = p.lower()
            if (set(p) - alphanum):
                return False
        return True

        

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            '172.16.254.1',
            'IPv4'
        ),
        (
            '2001:0db8:85a3:0:0:8A2E:0370:7334',
            'IPv6'
        ),
        (
            '256.256.256.256',
            'Neither'
        ),
        (
            "20EE:FGb8:85a3:0:0:8A2E:0370:7334",
            'IPv6'
        ),
    ]
    test(Solution().validIPAddress, test_data)

