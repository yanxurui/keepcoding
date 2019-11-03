from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        rst = []
        multiline = False
        line = []
        for l in source:
            i = 0
            while i < len(l):
                if multiline:
                    if l[i] == '*' and i < len(l)-1 and l[i+1] == '/':
                        multiline = False
                        i += 1
                    # else: ignore
                else:
                    if l[i] == '/' and i < len(l)-1 and l[i+1] == '/':
                        break # ignore the remaining of thie line
                    elif l[i] == '/' and i < len(l)-1 and l[i+1] == '*':
                        multiline = True
                        i += 1
                    else:
                        line.append(l[i])
                i += 1
            if not multiline and line:
                rst.append(''.join(line))
                line = []
        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [
                "/*Test program */",
                "int main()",
                "{ ",
                "  // variable declaration ",
                "int a, b, c;",
                "/* This is a test",
                "   multiline  ",
                "   comment for ",
                "   testing */",
                "a = b + c;",
                "}"
            ],
            ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
        ),
        (
            ["a/*comment", "line", "more_comment*/b"],
            ["ab"]
        ),
        (
            [
                "struct Node{",
                "    /*/ declare members;/**/", 
                "    int size;", 
                "    /**/int val;", 
                "};"
            ],
            ["struct Node{","    ","    int size;","    int val;","};"]
        ),
        (
            [
                "a/*/b//*c",
                "blank",
                "d/*/e*//f"
            ],
            ["ae*"]
        )
    ]
    test(Solution().removeComments, test_data)

