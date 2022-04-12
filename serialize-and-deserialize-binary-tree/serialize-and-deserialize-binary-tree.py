# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # I am thinking of having preorder traversal with L and R denoting left and right
        res = []
        def preorder(node):
            if node is None:
                res.append("None")
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        print(",".join(res))
        return ",".join(res)
        
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")
        if nodes[0] is None:
            return None
        root = TreeNode(nodes[0])
        def createTree(nodes, idx):
            if idx >= len(nodes):
                return 
            if nodes[idx] == "None":
                return (None, idx)
            node = TreeNode(int(nodes[idx]))
            node.left, i = createTree(nodes, idx+1)
            node.right, j = createTree(nodes, i+1)
            return (node, j)
        n = createTree(nodes, 0)
        return n[0]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))