class Solution:
	def longestCommonSubsequence(self, s1: str, s2: str) -> int:
		maxm = 0
		prev = [0]*(len(s1) + 1)
		for i in range(1, len(s2)+1):
			curr = [0]*(len(s1) + 1)
			for j in range(1, len(s1) + 1):
				curr[j] = max(curr[j-1], prev[j])
				if s2[i-1] == s1[j-1]:
					curr[j] = prev[j-1] + 1
					maxm = max(maxm, curr[j])
			prev = curr
		return maxm
				
        


