from collections import Counter
class Solution:
	def minSteps(self, s: str, t: str) -> int:
		countS = Counter(s)
		countT = Counter(t)
		res = 0
		for k, v in countS.items():
			if k not in countT:
				res += v
			elif countS[k] >= countT[k]:
				res += countS[k] - countT[k]
		return res
