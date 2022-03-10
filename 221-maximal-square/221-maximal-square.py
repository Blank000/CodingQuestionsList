class Solution:
	def maximalSquare(self, matrix: List[List[str]]) -> int:
		maxm = 0
		for i in range(len(matrix)):
			if (matrix[i][0] == "1"):
				matrix[i][0] = 1
				maxm = 1
			else:
				matrix[i][0] = 0

		for i in range(1,len(matrix[0])):
			if (matrix[0][i] == "1"):
				matrix[0][i] = 1
				maxm = 1
			else:
				matrix[0][i] = 0

		for i in range(1,len(matrix)):
			for j in range(1,len(matrix[0])):
				up, left, diag = math.inf, math.inf, math.inf
				if matrix[i][j] == "1":
					if i > 0:
						up = matrix[i-1][j]
					if j > 0:
						left = matrix[i][j-1]
					if i > 0 and j > 0:
						diag = matrix[i-1][j-1]
					val = min([up, left, diag]) + 1
					val = 1 if (val == math.inf) else val
					maxm = max(maxm, val)
					matrix[i][j] = val
				else:
					matrix[i][j] = 0
		return maxm**2
				
        


