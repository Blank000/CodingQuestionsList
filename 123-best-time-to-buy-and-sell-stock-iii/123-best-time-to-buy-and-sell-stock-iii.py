class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		# Gonna solve it with a general solution of k transactions 
		k = 2
		n = len(prices)
		dp = [[[-math.inf]*2 for _ in range(k+1)] for _ in range(n)] # dp[ith day][kth transaction][is holding stock or not]
		dp[0][0][0] = 0
		dp[0][1][1] = -prices[0]
		maxProfit = 0
		for i in range(1, n):
			for j in range(k+1):
				dp[i][j][0] = max(dp[i-1][j][1] + prices[i], dp[i-1][j][0])
				maxProfit = max(maxProfit, dp[i][j][0])
				if j > 0:
					dp[i][j][1] = max(dp[i-1][j][1] , dp[i-1][j-1][0] - prices[i])
		return maxProfit
					
