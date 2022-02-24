class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		res = []
		def order(nums, idx):
			if idx == len(nums):
				res.append(nums[:])
			for j in range(idx, len(nums)):
				nums[idx], nums[j] = nums[j], nums[idx]
				order(nums, idx+1)
				nums[idx], nums[j] = nums[j], nums[idx]
		order(nums, 0)
		return res
