class Solution:
	def findTargetSumWays(self, nums: List[int], target: int) -> int:
		dic = collections.defaultdict(int)
		dic[0] = 1
		for i in range(len(nums)):
			tempDic = dic.copy()
			dic.clear()
			for k,v in tempDic.items():
				dic[k+nums[i]] += v
				dic[k-nums[i]] += v
		return dic[target]
        


