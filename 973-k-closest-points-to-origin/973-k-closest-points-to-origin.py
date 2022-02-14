import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points
        distance = []
        maxmDist = 0
        for a, b in points:
            distance.append([a**2+b**2, a, b])
            maxmDist = max(maxmDist, distance[-1][0])
        low, high = 0, maxmDist
        res = []
        while k:
            mid = low + (high - low)//2
            closestTemp, farthestTemp = [], []
            for i in range(len(distance)):
                d, a, b, = distance[i]
                if d <= mid:
                    closestTemp.append([d, a, b])
                else:
                    farthestTemp.append([d, a, b])
            
            if len(closestTemp) > k:
                distance = closestTemp
                high = mid
            else:
                k -= len(closestTemp)
                res.extend(closestTemp)
                distance = farthestTemp
                low = mid
            
        return [[a,b] for _, a, b in res]