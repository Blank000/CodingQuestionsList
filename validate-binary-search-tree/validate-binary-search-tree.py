# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, minm, maxm):
            if node is None:
                return True
            return node.val > minm and node.val < maxm and dfs(node.left, minm, node.val) and dfs(node.right, node.val, maxm)
        return dfs(root, -math.inf, math.inf)
