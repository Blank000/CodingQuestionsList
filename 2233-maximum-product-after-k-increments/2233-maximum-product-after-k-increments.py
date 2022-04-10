import heapq
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0] + k
        heapq.heapify(nums)
        MOD = 10**9+7
        while k:
            firstMinm = heapq.heappop(nums)
            secondMinm = heapq.heappop(nums)
            #print(firstMinm, secondMinm)
            p = min(secondMinm-firstMinm + 1, k)
            k -= p
            firstMinm += p
            heapq.heappush(nums, firstMinm)
            heapq.heappush(nums, secondMinm)
        res = 1
        for n in nums:
            res *= n
            res %= MOD
        return res