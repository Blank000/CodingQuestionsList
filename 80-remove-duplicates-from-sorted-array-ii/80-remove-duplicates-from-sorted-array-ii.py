class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        k = 0
        while i < len(nums):
            curr = nums[i]
            nums[j] = curr
            j += 1
            i += 1
            if i < len(nums) and nums[i] == curr:
                nums[j] = nums[i]
                i += 1
                j += 1
            while i < len(nums) and nums[i] == curr:
                i += 1
        return j