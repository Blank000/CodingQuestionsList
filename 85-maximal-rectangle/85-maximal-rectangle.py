class Solution:
	def maximalRectangle(self, matrix: List[List[str]]) -> int:
		def getMaxAreaOfHistogram(arr):
			st = []
			maxArea, i = 0, 0
			while i < len(arr):
				if not st or arr[i] >= arr[st[-1]]:
					st.append(i)
					i += 1
				else:
					poppedIdx = st.pop()
					if st:
						area = (i - st[-1] - 1) * arr[poppedIdx]
					else:
						area = i * arr[poppedIdx]
					maxArea = max(maxArea, area)
			while st:
				poppedIdx = st.pop()
				if st:
					area = (i - st[-1] - 1) * arr[poppedIdx]
				else:
					area = i * arr[poppedIdx]
				maxArea = max(maxArea, area)
			return maxArea
					
		maxArea = 0
		prefixSum = [0]*len(matrix[0])
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j] == "1":
					matrix[i][j] = prefixSum[j] + 1
				else:
					matrix[i][j] = 0
			area = getMaxAreaOfHistogram(matrix[i])
			maxArea = max(maxArea, area)
			#print(area, matrix[i])
			prefixSum = matrix[i]
		return maxArea
