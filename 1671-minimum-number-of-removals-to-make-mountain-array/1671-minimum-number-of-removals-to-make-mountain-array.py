class Solution:
	def minimumMountainRemovals(self, nums: List[int]) -> int:
		# When I saw the graph I realised that we have to calculate the longest increasing sequence up until that point and move ahead from lleft to right and then right to left and find the point where it’s maxm
		lbs = [1]*len(nums)
		dp = [math.inf]*len(nums)
		for i in range(len(nums)):
			idx = bisect.bisect_left(dp, nums[i]) 
			lbs[i] = idx + 1
			dp[idx] = nums[i]
		dp = [math.inf]*len(nums)
		maxm = 1
		for i in range(len(nums)-1, -1, -1):
			idx = bisect.bisect_left(dp, nums[i])
			rbs = idx + 1
			if lbs[i] > 1 and rbs > 1:
				maxm = max(lbs[i] + rbs - 1, maxm)
			dp[idx] = nums[i]
		return len(nums) - maxm
			
