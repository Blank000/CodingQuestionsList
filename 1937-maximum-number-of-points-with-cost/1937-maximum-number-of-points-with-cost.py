class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # We will have the max value array for each previous row and as we proceed to the next row, for each element we will first calculate the maximum that we can get from the previous row values using a single variable as a pointer for maintaing the maximum current value
        prev = points[0]
        for i in range(1, len(points)):
            curr = 0
            temp = prev[:]
            for j in range(len(points[i])):
                curr = max(prev[j], curr-1)
                res = points[i][j] + curr
                temp[j] = res
            curr = 0
            for j in range(len(points[i])-1, -1, -1):
                curr = max(prev[j], curr-1)
                res = points[i][j] + curr
                prev[j] = max(temp[j], res)
        return max(prev)