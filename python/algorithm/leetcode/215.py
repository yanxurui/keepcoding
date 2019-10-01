class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def insert(self, head, v):
        p = head
        while p.next and p.next.val < v:
            p = p.next
        if v < head.val:
            newNode = ListNode(v)
            newNode.next = head
            return newNode
        else:
            if p.next:
                tmp = p.next
                p.next = ListNode(v)
                p.next.next = tmp
            else:
                p.next = ListNode(v)
            return head


    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        assert k <= len(nums)
        head = ListNode(nums[0])
        l = 1
        for i in range(1, len(nums)):
            head = self.insert(head, nums[i])
            if l + 1 > k:
                head = head.next
            else:
                l += 1
        return head.val


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            (
                [3,2,1,5,6,4],
                2
            ),
            5
        ),
        (
            (
                [3,2,3,1,2,4,5,5,6],
                4
            ),
            4
        )
    ]
    test(Solution().findKthLargest, test_data)
