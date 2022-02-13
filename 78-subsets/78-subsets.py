class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def backTrack(nums, idx, temp):
            subsets.append(temp)
            for i in range(idx, len(nums)):
                temp.append(nums[i])
                backTrack(nums, i+1, temp[:])
                temp.pop()
        backTrack(nums, 0, [])
        return subsets
    