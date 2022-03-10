class Solution:
	def minCut(self, s: str):
		# This is a typical question of palindrome to remind us to use the concept of enlarging radius from a center and check for even and odd palindromes using that
		if s == s[::-1]:
			return 0
		for i in range(len(s)):
			if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
				return 1
		cut = [x for x in range(-1, len(s))]
		for pos in range(len(s)):
			evenRadius, oddRadius = 0, 0
			# Assuming pos as the center
			# For odd pallindromes
			while pos-oddRadius >= 0 and pos+oddRadius < len(s) and s[pos-oddRadius] == s[pos+oddRadius]:
				cut[pos+oddRadius+1] = min(cut[pos+oddRadius+1], cut[pos-oddRadius] + 1)
				oddRadius += 1
			while pos-evenRadius >= 0 and pos+evenRadius+1 < len(s) and s[pos-evenRadius] == s[pos+evenRadius+1]:
				cut[pos+evenRadius+2] = min(cut[pos+evenRadius+2], cut[pos-evenRadius]+1)
				evenRadius += 1
		return cut[-1]



