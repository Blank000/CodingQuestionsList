"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if root is None:
            return 
        def input(res, node):
            res.append(node.val)
            for child in node.children:
                input(res, child)
        input(res, root)
        return res
