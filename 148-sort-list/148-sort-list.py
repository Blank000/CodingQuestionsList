class Solution:
	def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		def mergesort(head):
			if head is None:
				return
			if head.next is None:
				return head
			slow = head.next
			fast = head.next
			prev = head
			while fast and fast.next:
				prev = slow
				slow = slow.next
				fast = fast.next.next
			prev.next = None
			n1 = mergesort(head)
			n2 = mergesort(slow)
			return merge(n1, n2)
		def merge(node1, node2):
			if node1 is None:
				return node2
			if node2 is None:
				return node1
			ans = ListNode(-math.inf)
			curr = ans
			while node1 and node2:
				if node1.val > node2.val:
					curr.next = node2
					node2 = node2.next
					curr = curr.next
				else:
					curr.next = node1
					node1 = node1.next
					curr = curr.next
			if node1:
				curr.next = node1
			if node2:
				curr.next = node2
			return ans.next
		return mergesort(head)
