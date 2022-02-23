import bisect
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        i = 1
        localLen, maxLen = 1, 1
        while i < len(nums):
            if nums[i] > nums[i-1]:
                localLen += 1
                maxLen = max(maxLen, localLen)
            else:
                localLen = 1
            i += 1
        return maxLen