# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummyNode = ListNode(0)
        heap = []
        heapq.heapify(heap)
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, lists[i]))
        itr = dummyNode
        while heap:
            smallestElement, node = heap[0]
            while heap and heap[0][0] == smallestElement:
                smallestElement, node = heapq.heappop(heap)
                if node.next:
                    heapq.heappush(heap, (node.next.val, node.next))
                itr.next = ListNode(smallestElement)
                itr = itr.next
        return dummyNode.next