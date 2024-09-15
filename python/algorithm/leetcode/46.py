class Solution(object):
    def backtrack(self, nums, ans, tmp):
        if len(tmp) == len(nums):
            ans.append(list(tmp))
        else:
            for i in nums:
                if i not in tmp:
                    self.backtrack(nums, ans, tmp+[i])

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.backtrack(nums, ans, list())
        return ans


class Solution2(object):
    def dfs(self, nums, pos, ans):
        if pos == len(nums):
            ans.append(list(nums))
        else:
            for i in range(pos, len(nums)):
                nums[pos], nums[i] = nums[i], nums[pos] # swap
                self.dfs(nums, pos+1, ans)
                nums[pos], nums[i] = nums[i], nums[pos] # swap back

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(nums, 0, ans)
        return ans

class Solution3(object):
    def backtrack(self, nums, tmp, visited, ans):
        if len(tmp) == len(nums):
            ans.append(tmp)
        else:
            for i,n in enumerate(nums):
                if visited[i]:
                    continue
                visited[i] = True
                self.backtrack(nums, tmp+[n], visited, ans)
                visited[i] = False

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        visited = [False] * len(nums)
        self.backtrack(nums, [], visited, ans)
        return ans

if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            [1,2,3],
            [
                [1,2,3],
                [1,3,2],
                [2,1,3],
                [2,3,1],
                [3,1,2],
                [3,2,1]
            ]
        )
    ]
    test(Solution3().permute, test_data, compare=unordered_equal)

