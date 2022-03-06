class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
		wDict = {x: 1 for x in wordDict}
		breakpoints = [0]
		dic = collections.defaultdict(set)
		sentences = []
		for i in range(len(s)):
			for j in breakpoints:
				if s[j:i+1] in wDict:
					dic[j].add(s[j:i+1])
					breakpoints.append(i+1)
		if breakpoints[-1] != len(s):
			return []
		def createList(s, arr, idx):
			if idx == len(s):
				sentences.append(" ".join(arr))
				return
			for word in dic[idx]:
				arr.append(word)
				createList(s, arr, idx+len(word))
				arr.pop()
		createList(s, [], 0)
		return sentences
						
        

