import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = -1
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                break
            row = matrix[i]
            idx = bisect.bisect_left(row, target)
            if idx < len(row) and row[idx] == target:
                return True
        return False