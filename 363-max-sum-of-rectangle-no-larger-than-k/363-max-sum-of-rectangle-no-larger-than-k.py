import bisect
class Solution:
	def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
		# One extra thing from the maximum sum rectangle question of gfg we will learn here is prefix sum algorithm
		maxSum = -math.inf
		for i in range(len(matrix[0])):
			temp = [0]*len(matrix)
			for j in range(i, -1, -1):
				for n in range(len(matrix)):
					temp[n] += matrix[n][j]
				maxKadenSum = 0
				localSum = 0
				#print(i, j, temp)              
				for n in range(len(temp)):
					localSum += temp[n]
					if localSum < 0:
						localSum = 0
					maxKadenSum = max(maxKadenSum, localSum)
				if maxKadenSum == 0:
					maxKadenSum = max(temp)
				if maxKadenSum <= k:
					maxSum = max(maxSum, maxKadenSum)
				else:
					prefixSum = 0
					pr = [0]
					for n in range(len(temp)):
						prefixSum += temp[n]
						idx = bisect.bisect_left(pr, prefixSum - k)
						if idx < len(pr):
							maxSum = max(maxSum, prefixSum - pr[idx])
						bisect.insort(pr, prefixSum)
		return maxSum
