# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
    
    
    def bfsTraversal(self, node, val):
        arr = [node]
        temp = []
        while arr:
            for node in arr:
                if node.left is None:
                    node.left = TreeNode(val)
                    return node.val
                if node.right is None:
                    node.right = TreeNode(val)
                    return node.val
                else:
                    temp.append(node.left)
                    temp.append(node.right)
            arr = temp
        return -1
        
        
    def insert(self, val: int) -> int:
        #height = self.getHeight(self.root)
        return self.bfsTraversal(self.root, val)

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()