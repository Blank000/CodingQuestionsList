class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Find first ambiguity from the front and the rear and then between those find the minimum and the maximum element and then find the proper index for them
        startIdx, endIdx = -1, -1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                startIdx = i
                break
        for i in range(len(nums)-1, 0, -1):
            if nums[i] < nums[i-1]:
                endIdx = i
                break
        if startIdx == -1 and endIdx == -1:
            return 0
        minm, maxm = nums[startIdx], nums[endIdx]
        for i in range(startIdx, endIdx+1):
            minm, maxm = min(nums[i], minm), max(nums[i], maxm)
        i, j = 0, len(nums)-1
        while i < len(nums) and nums[i] <= minm:
            i += 1
        while j >= 0 and nums[j] >= maxm:
            j -= 1
        return j-i+1
        
            
                