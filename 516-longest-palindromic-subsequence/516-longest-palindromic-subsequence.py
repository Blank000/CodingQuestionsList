class Solution:
	def longestPalindromeSubseq(self, s1: str) -> int:
		# Same as LCS with the reversed string but now we are making use of the fact that we are searching for pallindromes
		dp = [[0]*(len(s1)+1) for _ in range(len(s1)+1)]
		for i in range(len(s1)):
			dp[i][i] = 1
		for i in range(len(s1)-1, -1, -1):
			for j in range(i+1, len(s1)):
				if s1[i] == s1[j]:
					dp[i][j] = dp[i+1][j-1] + 2
				else:
					dp[i][j] = max(dp[i+1][j], dp[i][j-1])
		return dp[0][len(s1)-1]

