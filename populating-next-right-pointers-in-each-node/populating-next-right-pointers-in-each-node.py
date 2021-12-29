"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        def bfs(arr):
            if len(arr) == 0:
                return
            temp = []
            for i in range(len(arr)-1):
                arr[i].next = arr[i+1]
                if arr[i].left:
                    temp.append(arr[i].left)
                if arr[i].right:
                    temp.append(arr[i].right)
            if arr[-1].left:
                temp.append(arr[-1].left)
            if arr[-1].right:
                temp.append(arr[-1].right)
            return bfs(temp)
        bfs([root])
        return root
                