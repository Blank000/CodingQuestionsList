class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)-1
        l = n.bit_length()
        res = 0
        for i in range(l):
            base_count, num_count = 0, 0  # Counts at (i+1)th bit position
            x = 1 << i
            for i in range(n+1):
                base_count += 1 if (x & i) > 0 else 0
                num_count += 1 if (x & nums[i]) > 0 else 0
            if num_count > base_count:
                res = res | x
        return res