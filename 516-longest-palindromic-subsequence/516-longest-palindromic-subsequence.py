class Solution:
	def longestPalindromeSubseq(self, s: str) -> int:
		# Same as LCS with the reversed string 
		prev = [0]*(len(s)+1)
		s1 = s[::-1]
		maxm = 1
		for i in range(1, len(s)+1):
			curr = [0]*(len(s)+1)
			for j in range(1,len(s1)+1):
				curr[j] = max(prev[j],curr[j-1])
				if s1[j-1] == s[i-1]:
					curr[j] = prev[j-1]+1
					maxm = max(maxm, curr[j])
			prev = curr
		return maxm
				
        

