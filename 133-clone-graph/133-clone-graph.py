"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        def deepcopy(node, visited):
            if node is None:
                return None
            if node.val in visited:
                return visited[node.val] 
            duplicate_node = Node(node.val)
            visited[node.val] = duplicate_node
            for neighbor in node.neighbors:
                duplicate_node.neighbors.append(deepcopy(neighbor, visited))
            return duplicate_node
        return deepcopy(node, visited)