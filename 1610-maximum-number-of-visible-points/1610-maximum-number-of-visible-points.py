class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        lx, ly = location
        radianAngle = math.pi * angle /180
        pointAngleFromLocationArr = [math.atan2(x-lx, y-ly) for x,y in points if (x != lx or y != ly)] + [2*math.pi + math.atan2(x-lx, y-ly) for x,y in points if x != lx or y != ly]
        numOfSamePoints = len([(x,y) for x,y in points if x == lx and y == ly])
        pointAngleFromLocationArr.sort()
        # Now it's like a slinding window problem where you will find the index i and j such that i <= j and pointAngleFromLocationArr[i]-pointAngleFromLocationArr[j] <= radianAngle
        i, j = 0, 0
        maxmNumberOfPointsExcludingLocationPoints = 0
        while j < len(pointAngleFromLocationArr):
            if pointAngleFromLocationArr[j] - pointAngleFromLocationArr[i] <= radianAngle:
                maxmNumberOfPointsExcludingLocationPoints = max(maxmNumberOfPointsExcludingLocationPoints, j-i+1)
                j += 1
            else:
                i += 1
        #maxmNumberOfPointsExcludingLocationPoints = max(maxmNumberOfPointsExcludingLocationPoints, j-i+1)
        return maxmNumberOfPointsExcludingLocationPoints + numOfSamePoints