class Solution:
	def partition(self, s: str) -> List[List[str]]:
		dp = [[False]*(len(s)) for _ in range(len(s))]
		for i in range(len(s)):
			dp[i][i] = True
		for l in range(1, len(s)):
			for i in range(len(s)-l):
				if s[i:i+l+1] == s[i:i+l+1][::-1]:
					dp[i][i+l]  = True
		res = []
		def createArr(dp, row, col, temp):
			temp.append(s[row:col+1])
			if col == len(dp[0])-1:
				res.append(temp)
				return
			row = col+1
			for i in range(row, len(dp[0])):
				if s[row:i+1] == s[row:i+1][::-1]:
					createArr(dp, row, i, temp[:])
		for i in range(len(dp[0])):
			if s[:i+1] == s[:i+1][::-1]:
				createArr(dp, 0, i,[])
		return res
        


