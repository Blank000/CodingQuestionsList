import heapq
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        maxHeap = []
        maxValue = float("-inf")
        for x,y in points:
            while maxHeap and x - maxHeap[0][1] > k:
                heapq.heappop(maxHeap)
            if maxHeap:
                maxValue = max(maxValue, x+y + (-maxHeap[0][0]))
            heapq.heappush(maxHeap, (x-y, x))
        return maxValue
            