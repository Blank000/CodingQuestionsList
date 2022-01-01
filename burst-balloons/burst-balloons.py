class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # This is a very good question on DP which can't be solved easily. The unoptimised solution one might come up with but the optimised one is really tough to come with. So the concept is to come up with the last balloon to burst and keep seggregating the array and slowly move up
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]
        nums = [1] + nums + [1]
        left, right = 1, len(nums)-2
        @lru_cache(None)
        def burstLastBalloon(left, right):
            if left > right:
                return 0
            maxm = 0
            for i in range(left, right+1):
                gain = nums[i]*nums[left-1]*nums[right+1]
                remaining = burstLastBalloon(left, i-1) + burstLastBalloon(i+1, right)
                maxm = max(maxm, gain+remaining)
            return maxm
        return burstLastBalloon(left, right)