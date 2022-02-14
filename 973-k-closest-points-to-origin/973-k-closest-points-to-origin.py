import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for a, b in points:
            heapq.heappush(heap, (a**2+b**2, a, b))
        res = []
        while k:
            _, a, b = heapq.heappop(heap)
            res.append([a,b])
            k -= 1
        return res