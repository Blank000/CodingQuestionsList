import random
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = math.ceil(len(nums)/2)
        while True:
            v = random.choice(nums)
            count = len([1 for elem in nums if elem == v])
            if count >= n:
                return v
        