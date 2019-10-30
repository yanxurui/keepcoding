class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        new_path = []
        prev = None
        for p in path.split('/'):
            if p == '' or p == '/' or p == '.':
                continue
            elif p == '..':
                if len(new_path) > 0:
                    new_path.pop()
            else:
                new_path.append(p)
        return '/' + '/'.join(new_path)        
          

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            "/home/",
            "/home"
        ),

        (
            "/../",
            "/"
        ),

        (
            "/home//foo/",
            "/home/foo"
        ),

        (
            "/a/./b/../../c/",
            "/c"
        ),

        (
            "/a/../../b/../c//.//",
            "/c"
        ),

        (
            "/a//b////c/d//././/..",
            "/a/b/c"
        ),
    ]
    test(Solution().simplifyPath, test_data)
