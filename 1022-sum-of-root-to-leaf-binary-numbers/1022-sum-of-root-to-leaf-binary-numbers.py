# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(node, arr):
            if node is None:
                return
            if node.left is None and node.right is None:
                res.append(arr+[str(node.val)])
                return
            dfs(node.left, arr+[str(node.val)])
            dfs(node.right, arr+[str(node.val)])
        dfs(root, [])
        #print(res)
        return sum([int("".join(a),2) for a in res])
            