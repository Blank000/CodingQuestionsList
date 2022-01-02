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
        def getClosingBracketIdx(s, idx):
            if idx >= len(s) or s[idx] != "(":
                return idx
            no = 1
            for i in range(idx+1, len(s)):
                if s[i] == "(":
                    no += 1
                elif s[i] == ")":
                    no -= 1
                if no == 0:
                    return i
            return -1
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
        def constructTree(s, left, right):
            if left >= len(s) or left >= right or s[left] != "(":
                return
            n, idx = getNum(s, left+1)
            node = TreeNode(n)
            if idx < len(s) and s[idx] == "(":
                leftCbIdx = getClosingBracketIdx(s, idx)
                node.left = constructTree(s, idx, leftCbIdx)
                rightCbIdx = getClosingBracketIdx(s, leftCbIdx+1)
                node.right = constructTree(s, leftCbIdx+1, rightCbIdx)
            return node
        s = "("+s+")"
        '''
        node = TreeNode(int(s[0]))
        leftCbIdx = getClosingBracketIdx(s, 1)
        node.left = constructTree(s, 1, leftCbIdx)
        rightCbIdx = getClosingBracketIdx(s, leftCbIdx+1)
        node.right = constructTree(s, leftCbIdx+1, len(s)-1)
        
        left = 0 if node.left is None else node.left.val
            right = 0 if node.right is None else node.right.val
            print(node.val, left, right)
        '''
        return constructTree(s, 0, len(s)-1)