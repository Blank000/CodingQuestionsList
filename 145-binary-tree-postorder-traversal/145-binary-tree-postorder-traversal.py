class Solution:
	def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		res = []
		st = []
		curr = root
		while curr or st:
			while curr:
				st.append(curr)
				curr = curr.left
			topElememt = st[-1]
			if topElememt.right:
				curr = topElememt.right
			else:
				poppedElement = st.pop()
				res.append(poppedElement.val)
				while st and st[-1].right == poppedElement:
					poppedElement = st.pop()
					res.append(poppedElement.val) 
		return res
