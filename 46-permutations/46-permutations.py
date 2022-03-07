from collections import Counter
class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		dic = Counter(nums)
		result = []
		def permute(temp) :
			if len(temp) == len(nums):
				result.append(temp[:])
				return
			for key in dic:
				if dic[key] > 0:
					dic[key] -= 1
					temp.append(key)
					permute(temp)
					temp.pop()
					dic[key] += 1
		permute([])
		return result