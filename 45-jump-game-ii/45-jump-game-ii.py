class Solution:
    def jump(self, nums: List[int]) -> int:
        farthestIdx = 0
        jumps = 0
        currentEnd = 0
        for i in range(len(nums)-1):
            farthestIdx = max(farthestIdx, i+nums[i])
            if i == currentEnd:
                jumps += 1
                currentEnd = farthestIdx
        return jumps