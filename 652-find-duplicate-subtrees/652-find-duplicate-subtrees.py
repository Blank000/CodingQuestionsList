# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        '''
         Inorder traversals can tell you about symmetric trees and pre and post orders can tell about the 
         duplicate trees
         So idea is to create postorder traversal string and compare it if it exists
        '''
        
        dic = {}
        res = []
        def postOrderTraversal(node):
            if node is None:
                return ""
            key = postOrderTraversal(node.left) + " " + postOrderTraversal(node.right) + " " + str(node.val)
            if key in dic:
                if dic[key] == 1:
                    res.append(node)
                    dic[key] = 0 
            else:
                dic[key] = 1
            return key
        postOrderTraversal(root)
        return res
            