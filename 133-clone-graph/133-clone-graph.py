"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dic = {}
        def deepCopy(node, dic):
            if node is None:
                return 
            if node.val in dic:
                return dic[node.val]
            rootCopy = Node(node.val)
            dic[node.val] = rootCopy
            for neighbor in node.neighbors:
                rootCopy.neighbors.append(deepCopy(neighbor, dic))
            return rootCopy
        return deepCopy(node, dic)