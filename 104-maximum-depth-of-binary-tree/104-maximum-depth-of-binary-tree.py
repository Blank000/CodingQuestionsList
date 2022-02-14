# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getHeight(node, height):
            if node is None:
                return height
            return max(getHeight(node.left, height+1), getHeight(node.right, height+1))
        return getHeight(root, 0)