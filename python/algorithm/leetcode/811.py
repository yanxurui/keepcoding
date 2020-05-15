from typing import List
from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)        
        for cnt_domain in cpdomains:
            cnt, domain = cnt_domain.split(' ')
            cnt = int(cnt)
            d[domain] += cnt
            for i in range(len(domain)):
                if domain[i] == '.':
                    sub = domain[i+1:]
                    d[sub] += cnt
        rst = []
        for sub, cnt in d.items():
            rst.append('%d %s' % (cnt, sub))
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            ["9001 discuss.leetcode.com"],
            ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
        ), 
        (
            ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"],
            ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
        )
    ]
    test(Solution().subdomainVisits, test_data, compare=unordered_equal)

