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
        visitedP = set()
        visitedQ = set()
        while p and q:
            if p.val == q.val or p.val in visitedQ:
                return p
            if q.val in visitedP:
                return q
            visitedP.add(p.val)
            visitedQ.add(q.val)
            p = p.parent
            q = q.parent
        if p is None:
            while q:
                if q.val in visitedP:
                    return q
                q = q.parent
        if q is None:
            while p:
                if p.val in visitedQ:
                    return p
                p = p.parent