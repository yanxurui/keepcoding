def sort_nest(L):
    for i in range(len(L)):
        if isinstance(L[i], list):
            L[i] = sort_nest(L[i])
    return sorted(L)

def nested_unordered_equal(a, b):
    '''compare 2 unordered nested list
    '''
    return len(a) == len(b) and sort_nest(a) == sort_nest(b)

def unordered_equal(a, b):
    return len(a) == len(b) and sorted(a) == sorted(b)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def create(cls, vals):
        head = None
        p = None
        for v in vals:
            n = cls(v)
            if head is None:
                head = n
                p = head
            else:
                p.next = n
                p = n
        return head

    def __eq__(p, q):
        while p and q:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return p is None and q is None

    def __str__(p):
        vals = []
        while p is not None:
            vals.append(p.val)
            p = p.next
        return str(vals)


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def create(cls, vals):
        queue = []
        root = None
        parent = None
        for v in vals:
            if v is None:
                node = None
            else:
                node = cls(v)
            if root is None:
                root = node
            elif parent is None:
                while True: # skip None
                    parent = queue.pop(0)
                    if parent:
                        break
                parent.left = node
            else:
                parent.right = node
                parent = None
            if node:
                queue.append(node)
        return root

    def to_list(root):
        queue = [root]
        vals = []
        while queue:
            node = queue.pop(0)
            if node:    
                vals.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                vals.append(None)
        while len(vals) > 1 and vals[-1] is None:
            vals.pop()
        return vals


    def __repr__(root):
        return str(root.to_list())

    def __eq__(self, other):
        return str(self) == str(other)
    def __lt__(self, other):
        return str(self) < str(other)