class Solution:
	def findNumberOfLIS(self, nums: List[int]) -> int:
		dp = [[1,1] for _ in range(len(nums))] # [Length of largest LIS, num of occurences]
		maxLen = 1
		numOfOcc = 0
		for i in range(len(nums)):
			for j in range(i):
				if nums[i] > nums[j]:
					if dp[j][0] + 1 == dp[i][0]:
						dp[i][1] += dp[j][1]
					elif dp[j][0] + 1 > dp[i][0]:
						dp[i] = [dp[j][0]+1, dp[j][1]]
						if dp[i][0] > maxLen:
							maxLen = dp[i][0]
		for i in range(len(dp)):
			if dp[i][0] == maxLen:
				numOfOcc += dp[i][1]
		#print(maxLen, dp)
		return numOfOcc
					



