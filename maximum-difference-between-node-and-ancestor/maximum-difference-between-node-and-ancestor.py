# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        diff = 0
        def get(node):
            if node is None:
                return (float("inf"), float("-inf"))
            nonlocal diff
            minLeft, maxLeft = get(node.left)
            minRight, maxRight = get(node.right)
            minm = min(node.val, min(minLeft, minRight))
            maxm = max(node.val, max(maxLeft, maxRight))
            if node.right:
                diff = max(diff, abs(maxRight-node.val))
                diff = max(diff, abs(minRight-node.val))
            if node.left:
                diff = max(diff, abs(minLeft-node.val))
                diff = max(diff, abs(maxLeft-node.val))
            return (minm, maxm)
        get(root)
        return diff