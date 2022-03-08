class Solution:
	def canJump(self, nums: List[int]) -> bool:
		maxIdx, i = 0, 0
		while i < len(nums) and maxIdx >= i:
			maxIdx = max(maxIdx, i + nums[i])
			if maxIdx == len(nums)-1:
				return True
			i += 1
		if maxIdx < i:
			return False
		return True
