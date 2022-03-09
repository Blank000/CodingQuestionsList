class Solution:
	def PredictTheWinner(self, nums: List[int]) -> bool:
		dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
		for i in range(len(nums)):
			dp[i][i] = nums[i]
		for l in range(1, len(nums)):
			for i in range(len(nums)-l):
				dp[i][i+l] = max(nums[i] - dp[i+1][i+l], nums[i+l] - dp[i][i+l-1])
		return dp[0][len(nums)-1] >= 0


