class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        maxmHeight = 0
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > maxmHeight:
                res.append(i)
            maxmHeight = max(maxmHeight, heights[i])
        return res[::-1]