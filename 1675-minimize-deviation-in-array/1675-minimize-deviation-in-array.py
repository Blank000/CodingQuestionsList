import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        minm = float("inf")
        minmDev = float("inf")
        for i in range(len(nums)):
            if nums[i]&1 == 1:
                heapq.heappush(heap, -nums[i]*2)
                minm = min(nums[i]*2, minm)
            else:
                heapq.heappush(heap, -nums[i])
                minm = min(nums[i], minm)
        
        while heap and heap[0]&1 == 0:
            n = heapq.heappop(heap)
            heapq.heappush(heap, n//2)
            minm = min(minm, -n//2)
            minmDev = min(minmDev, abs(-heap[0] - minm))
        return minmDev
                