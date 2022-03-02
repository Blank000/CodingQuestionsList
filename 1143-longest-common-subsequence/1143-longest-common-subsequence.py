class Solution:
	def longestCommonSubsequence(self, s1: str, s2: str) -> int:
		# First is the brute force method
		dp = [[0]*(len(s1)+1)  for _ in range(len(s2)+1)]
		for i in range(len(s2)+1):
			dp[i][0] = 0
		for i in range(len(s1)+1):
			dp[0][i] = 0
		maxm = 0
		for i in range(1,len(s2)+1):
			for j in range(1,len(s1)+1):
				dp[i][j] = max(max(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])
				if s1[j-1] == s2[i-1]:
					dp[i][j] = dp[i-1][j-1] + 1
					maxm = max(maxm, dp[i][j])
		return maxm
			
		
        


