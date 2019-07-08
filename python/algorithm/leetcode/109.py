# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/discuss/35476/Share-my-JAVA-solution-1ms-very-short-and-concise.

from common import ListNode, TreeNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        else:
            return self.toBST(head, None)

    def toBST(self, head, tail):
        if head == tail:
            return None
        slow, fast = head, head
        while fast.next != tail and fast.next.next != tail:
            fast = fast.next.next
            slow = slow.next
        root = TreeNode(slow.val)
        root.left = self.toBST(head, slow)
        root.right = self.toBST(slow.next, tail)
        return root
        

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            ListNode.create([0, -10, 5, None, -3, None, 9]),
            TreeNode.create([0,-3,9,-10,None,5])
        ),
        (
            ListNode.create([]),
            None
        )
    ]
    test(Solution().sortedListToBST, test_data)

