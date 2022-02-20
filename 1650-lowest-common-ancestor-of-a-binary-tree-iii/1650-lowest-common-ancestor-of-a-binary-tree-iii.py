"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        dicP = {}
        dicQ = {}
        while p and q:
            dicP[p.val] = p
            dicQ[q.val] = q
            if p.val in dicQ:
                return dicQ[p.val]
            if q.val in dicP:
                return dicP[q.val]
            p = p.parent
            q = q.parent
        while p:
            if p.val in dicQ:
                return dicQ[p.val]
            p = p.parent
        while q:
            if q.val in dicP:
                return dicP[q.val]
            q = q.parent
        return