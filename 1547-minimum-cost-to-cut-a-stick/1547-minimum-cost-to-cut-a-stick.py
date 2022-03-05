class Solution:
	def minCost(self, n: int, cuts: List[int]) -> int:
		# Think of this in reverse manner that some pieces are given to you and you need to stick them with minimum cost where the cost of sticking is equal to the length of sum of those two pieces
		cuts = [0] + cuts + [n]
		cuts.sort()
		dp = [[math.inf]*(len(cuts)) for _ in range(len(cuts))]
		for l in range(1,len(cuts)):
			for i in range(len(cuts) - l):
				if l == 1:
					dp[i][i+l] = 0
				else:
					for j in range(i+1, i+l):
						dp[i][i+l] = min(dp[i][i+l] , dp[i][j] + dp[j][i+l] - cuts[i] + cuts[i+l])
		return dp[0][len(cuts)-1]