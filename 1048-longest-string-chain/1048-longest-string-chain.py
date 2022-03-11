class Solution:
	def longestStrChain(self, words: List[str]) -> int:
		words.sort(key = len)
		dp = [1]*len(words)
		currLen = len(words[0])
		startIdx, lastIdx = 0, 0
		for i in range(len(words)):
			if len(words[i]) > currLen:
				startIdx, lastIdx = lastIdx, i
				currLen = len(words[i])
			for j in range(startIdx, lastIdx):
				if len(words[i])-len(words[j]) == 1:
					for k in range(len(words[i])):
						if words[i][:k]+words[i][k+1:] == words[j]:
							dp[i] = max(dp[i], dp[j] + 1)
				else:
					break
		return max(dp)
