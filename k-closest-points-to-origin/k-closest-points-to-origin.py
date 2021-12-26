import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for x,y in points:
            dis = math.sqrt(x**2+y**2)
            heapq.heappush(heap, (dis, x, y))
        res = []
        while k:
            _, x, y = heapq.heappop(heap)
            res.append([x,y])
            k -= 1
        return res