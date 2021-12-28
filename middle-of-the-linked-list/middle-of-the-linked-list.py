# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        l = 1
        itr = head
        while itr:
            itr = itr.next
            l += 1
        mid = (l-1) // 2 
        itr = head
        while mid:
            itr = itr.next
            mid -= 1
        return itr