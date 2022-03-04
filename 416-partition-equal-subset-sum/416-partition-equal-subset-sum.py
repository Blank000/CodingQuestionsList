class Solution:
	def canPartition(self, nums: List[int]) -> bool:
		summ = sum(nums)
		if summ&1 != 0:
			return False
		summ = summ // 2
		prev = [False]*(summ+1)
		prev[0] = True
		for i in range(len(nums)):
			curr = [False]*(summ + 1)
			curr[0] = True
			for j in range(summ + 1):
				curr[j] = prev[j]
				if j >= nums[i]:
					curr[j] = curr[j] or prev[j-nums[i]]
			prev = curr
		return prev[-1]
		
				


