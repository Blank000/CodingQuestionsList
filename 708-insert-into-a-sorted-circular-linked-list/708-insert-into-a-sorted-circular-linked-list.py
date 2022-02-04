"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            node = Node(insertVal)
            node.next = node
            return node
        itr = head.next
        smallest, largest = head.val, head.val
        while itr != head:
            smallest = min(smallest, itr.val)
            largest = max(largest, itr.val)
            itr = itr.next        
        if insertVal <= smallest or insertVal >= largest:
            itr = head
            while not (itr.val >= largest and itr.next.val <= smallest):
                itr = itr.next
            nextNode = itr.next
            itr.next = Node(insertVal)
            itr.next.next = nextNode
        else:
            itr = head
            while not (itr.val <= insertVal and itr.next.val >= insertVal):
                itr = itr.next
            nextNode = itr.next
            itr.next = Node(insertVal)
            itr.next.next = nextNode
        return head