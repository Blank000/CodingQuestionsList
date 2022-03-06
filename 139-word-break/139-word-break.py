class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		dic = {}
		for word in wordDict:
			dic[word] = 1
		breakpoints = [-1]
		for i in range(len(s)):
			for j in range(len(breakpoints)-1, -1, -1):
				if s[breakpoints[j]+1:i+1] in wordDict:
					breakpoints.append(i)
					break
		if breakpoints[-1] == len(s)-1:
			return True
		return False

