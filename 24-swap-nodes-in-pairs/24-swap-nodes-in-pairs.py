# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        if head.next is None:
            return head
        prev, curr, next = None, head, head.next
        root = head.next
        while next:
            curr.next, next.next = next.next, curr
            if prev:
                prev.next = next
            prev = curr
            if curr.next and curr.next.next:
                curr, next = curr.next, curr.next.next
            else:
                break
        return root