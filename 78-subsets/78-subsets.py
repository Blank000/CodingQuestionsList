class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        nth_bit = 1 << n
        for i in range(2**n):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i | nth_bit)[3:]
            output.append([nums[j] for j in range(len(nums)) if bitmask[j] == "1"])
        return output