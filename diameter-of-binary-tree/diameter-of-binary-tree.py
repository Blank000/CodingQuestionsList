# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxm = 1
        def inorder(node):
            if node is None:
                return 0
            nonlocal maxm
            left = inorder(node.left)
            right = inorder(node.right)
            maxm = max(maxm, left+right+1)
            return max(left, right) + 1
        inorder(root)
        return maxm-1