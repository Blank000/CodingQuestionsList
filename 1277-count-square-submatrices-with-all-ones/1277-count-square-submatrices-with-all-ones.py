class Solution:
	def countSquares(self, matrix: List[List[int]]) -> int:
		# Simple dp problem
		summ = 0
		for i in range(len(matrix)):
			summ += matrix[i][0]
		for i in range(1,len(matrix[0])):
			summ += matrix[0][i]
		for i in range(1,len(matrix)):
			for j in range(1,len(matrix[0])):
				if matrix[i][j] == 1:
					matrix[i][j] = max(min([matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]]) + 1, 1)
					summ += matrix[i][j]
		return summ
			


