class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # Distance between any point to teo points will be the side length and the third one must be the diagonal
        def getDistance(p1, p2):
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
        dis = set()
        points = [p1, p2, p3, p4]
        for i in range(len(points)):
            dis = set()
            for j in range(len(points)):
                if i != j:
                    dis.add(getDistance(points[i], points[j]))
            if len(dis) != 2 or 2*min(dis) != max(dis):
                return False
        return True