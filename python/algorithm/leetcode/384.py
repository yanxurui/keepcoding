from typing import List
from random import randint

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.

        proof:

        let's consider the probability of the ith element being placed at position j in [1, n]
        when processing ele i,
            it can be swapped to any position between [1, i]
            so it has probability 1/i to be placed at any position in [1, i]
        wehn processing ele i+1
            i can be swapped to i+1, the probability is (1/i)*i * 1/(i+1) = 1/(i+1)
            when i is not selected, the probability of i being at a position j in [1, i] is 1/i * (1-(1/(1+i))) = 1/(i+1)
        so on and so forth
        that is, the probability of an element i being placed at any position in [1, n] is 1/n
        """
        rst = list(self.nums)
        for i in range(1, len(self.nums)):
            j = randint(0, i) # [0,i]
            self._swap(rst, i, j)
        return rst

    def _swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

        


# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3])
assert obj.reset() == [1,2,3]
print(obj.shuffle())
