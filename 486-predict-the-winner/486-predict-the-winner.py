class Solution:
	def PredictTheWinner(self, nums: List[int]) -> bool:
		dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
		for i in range(len(nums)):
			dp[i][i] = nums[i]
		for i in range(len(nums)-1):
			dp[i][i+1] = max(nums[i], nums[i+1])
		for l in range(2, len(nums)):
			for i in range(len(nums)-l):
				dp[i][i+l] = max(nums[i] + min(dp[i+2][i+l], dp[i+1][i+l-1]), nums[i+l] + min(dp[i+1][i+l-1], dp[i][i+l-2]))
		return dp[0][len(nums)-1] >= sum(nums) - dp[0][len(nums)-1] 

