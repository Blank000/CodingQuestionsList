# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        '''
        So basically it's the inorder traversal of a binary tree so the traversal will look like
        node, left , right so, for each bracket we are gonna search for it's corresponding closing bracket
        ''' 
        if len(s) == 0:
            return
        def isDigit(c):
            if ord(c) >= 48 and ord(c) <= 57:
                return True
            return False
        
        def getNum(s, idx):
            sign = 1
            if s[idx] == "-":
                sign = -1
                idx += 1
            res = 0
            while idx < len(s) and isDigit(s[idx]):
                res = 10*res + int(s[idx])
                idx += 1
            return (sign*res, idx)
        def constructTree(s, idx):
            if idx == len(s):
                return None, idx
            n, idx = getNum(s, idx)
            node = TreeNode(n)
            if idx < len(s) and s[idx] == "(":
                node.left, idx = constructTree(s, idx+1)
            if node.left and idx < len(s) and s[idx] == "(":
                node.right, idx = constructTree(s, idx+1)
            return (node, idx+1 if idx < len(s) and s[idx] == ")" else idx )
        #s = "("+s+")"
        node, idx = constructTree(s, 0)
        return node