class Solution:
	def longestCommonSubsequence(self, s1: str, s2: str) -> int:
		# Second solution that we are presenting here is a space optimised solution
		prev = [0]*(len(s1)+1)
		maxm = 0
		for i in range(1, len(s2)+1):
			curr = [0]*(len(s1)+1)
			for j in range(1, len(s1)+1):
				curr[j] = max(curr[j-1], max(prev[j-1], prev[j]))
				if s2[i-1] == s1[j-1]:
					curr[j] = prev[j-1] + 1
					maxm = max(curr[j], maxm)
			prev = curr
		return maxm
		
			
		
        


