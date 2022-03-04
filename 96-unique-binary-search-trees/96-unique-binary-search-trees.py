class Solution:
	def numTrees(self, n: int) -> int:
		if n == 0 or n == 1:
			return 1
		num = 1
		den = 1
		for k in range(2, n+1):
			num *= (n+k)
			den *= k
		return (num//den)
