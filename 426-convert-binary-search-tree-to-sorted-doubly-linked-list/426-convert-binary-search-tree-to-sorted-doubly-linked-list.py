"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def traverse(node):
            head, tail = node, node
            if node.left:
                head, tailLeft = traverse(node.left)
                tailLeft.right = node
                node.left = tailLeft
            if node.right:
                headRight, tail = traverse(node.right)
                headRight.left = node
                node.right = headRight
            return head, tail
        if root is None:
            return
        head, tail = traverse(root)
        tail.right = head
        head.left = tail
        return head