# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.l = 0
        self.head = head
        itr = head
        while itr:
            itr = itr.next
            self.l += 1
        

    def getRandom(self) -> int:
        if self.head is None:
            return
        ra = random.randint(1,self.l)
        itr = self.head
        idx = 1
        while idx < ra:
            itr = itr.next
            idx += 1
        return None if not itr else itr.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()