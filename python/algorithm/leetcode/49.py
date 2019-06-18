from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = defaultdict(list)
        for w in strs:
            ans[''.join(sorted(w))].append(w)
        return list(ans.values())

if __name__ == '__main__':
    from testfunc import test
    def sort_nest(L):
        for i in range(len(L)):
            if isinstance(L[i], list):
                L[i] = sort_nest(L[i])
        return sorted(L)

    def compare(a, b):
        '''compare 2 unordered nested list
        '''
        return len(a) == len(b) and sort_nest(a) == sort_nest(b)

    test_data = [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [
                ["ate","eat","tea"],
                ["nat","tan"],
                ["bat"]
            ]
        )
    ]
    test(Solution().groupAnagrams, test_data, compare=compare)

