# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summ = 0
        curr = root
        st = []
        while st or curr:
            while curr:
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            if curr.val > high:
                return summ
            if curr.val >= low:
                summ += curr.val
            curr = curr.right
        return summ