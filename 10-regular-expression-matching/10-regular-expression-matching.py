class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
		dp[0][0] = True
		for i in range(2, len(p)+1):
			if p[i-1] == "*":
				dp[0][i] = dp[0][i-2]
		for i in range(1,len(dp)):
			for j in range(1,len(dp[0])):
				if s[i-1] == p[j-1] or p[j-1] == ".":
					dp[i][j] = dp[i-1][j-1]
				elif p[j-1] == "*" :
					if (s[i-1] == p[j-2]) or p[j-2] == ".":
						dp[i][j] = dp[i-1][j]
					dp[i][j] = dp[i][j] or dp[i][j-2]
		return dp[-1][-1]




