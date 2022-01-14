class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        nonOverlapping = 0
        endMin = float("inf")
        points.sort()
        for p in points:
            if p[0] > endMin:
                count += 1
                nonOverlapping = 1
                endMin = p[1]
            else:
                nonOverlapping += 1
                endMin = min(endMin, p[1])
        return count + 1 
    
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        nonOverlapping = 1
        endMin = float("inf")
        points.sort()
        for p in points:
            if p[0] >= endMin:
                count += (nonOverlapping-1)
                nonOverlapping = 1
                endMin = p[1]
            else:
                nonOverlapping += 1
                endMin = min(endMin, p[1])
        return count + nonOverlapping - 1
'''