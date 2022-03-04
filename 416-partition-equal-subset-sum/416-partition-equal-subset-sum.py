class Solution:
	def canPartition(self, nums: List[int]) -> bool:
		# Solving using bit masking 
		s = sum(nums)
		if s & 1:
			return False
		n = 1
		for i in range(len(nums)):
			n = n | n << nums[i] 
		return n & 1 << s//2