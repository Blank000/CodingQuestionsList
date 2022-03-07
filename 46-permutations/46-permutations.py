class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		result = []
		def backtrack(arr, left, right):
			if left == len(arr):
				result.append(arr[:])
			for i in range(left, right+1):
				arr[left], arr[i] = arr[i], arr[left]
				backtrack(arr, left+1, right)
				arr[left], arr[i] = arr[i], arr[left]
		backtrack(nums, 0, len(nums)-1)
		return result