# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        if root.val not in to_delete:
            res.append(root)
        def traversal(node, parent, toDel, isLeft):
            if node is None:
                return
            if node.val in toDel and parent:
                if isLeft:
                    parent.left = None
                else:
                    parent.right = None
            if node.left:
                if node.val in toDel and node.left.val not in toDel:
                    res.append(node.left)
                traversal(node.left, node, toDel, True)
            if node.right:
                if node.val in toDel and node.right.val not in toDel:
                    res.append(node.right)
                traversal(node.right, node, toDel, False)
        traversal(root, None, to_delete, True)
        return res