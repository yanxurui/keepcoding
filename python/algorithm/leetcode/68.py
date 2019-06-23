class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ans = []
        line = []
        l = 0
        import pdb
        # pdb.set_trace()
        for w in words:
            if l + len(w) <= maxWidth:
                line.append(w)
                l += len(w) + 1
            else:
                l -= 1
                if len(line) == 1:
                    new_line = line
                    new_line.append(' '*(maxWidth-l))
                else:
                    blank_num = len(line) - 1
                    pad = [1] * blank_num
                    for i in range(maxWidth - l):
                        pad[i%blank_num] += 1
                    new_line = []
                    for i, p in enumerate(pad):
                        new_line.append(line[i])
                        new_line.append(' ' * p)
                    new_line.append(line[-1])
                ans.append(new_line)
                
                line = [w]
                l = len(w) + 1

        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        ans = [''.join(line) for line in ans]
        ans.append(last_line)
        return ans

        
if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            (
                ["This", "is", "an", "example", "of", "text", "justification."],
                16
            ),
            [
               "This    is    an",
               "example  of text",
               "justification.  "
            ]
        ),
        (
            (
                ["What","must","be","acknowledgment","shall","be"],
                16
            ),
            [
              "What   must   be",
              "acknowledgment  ",
              "shall be        "
            ]
        ),
        (

            (
                ["Science","is","what","we","understand","well","enough","to","explain",
                     "to","a","computer.","Art","is","everything","else","we","do"],
                20
            ),
            [
              "Science  is  what we",
              "understand      well",
              "enough to explain to",
              "a  computer.  Art is",
              "everything  else  we",
              "do                  "
            ]
        )

    ]
    test(Solution().fullJustify, test_data)
