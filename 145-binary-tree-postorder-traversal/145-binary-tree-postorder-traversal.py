class Solution:
	def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		res = []
		def recurse(node):
			if node is None:
				return
			recurse(node.left)
			recurse(node.right)
			res.append(node.val)
		recurse(root)
		return res

