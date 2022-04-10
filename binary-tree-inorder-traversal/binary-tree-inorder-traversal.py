# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        curr = root
        res = []
        st = []
        while st or curr:
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                curr = st.pop()
                res.append(curr.val)
                curr = curr.right
        return res