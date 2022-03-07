class Solution:
	def kIncreasing(self, arr: List[int], k: int) -> int:
		# Make a new array with elements starting from a certain index with k steps 
		def createNewList(arr, idx, k):
			temp = []
			for i in range(idx, len(arr), k):
				temp.append(arr[i])
			return temp
		def getLISwithRepeatedElement(arr):
			dp = []
			for i in range(len(arr)):
				idx = bisect.bisect_right(dp, arr[i])
				if idx == len(dp):
					dp.append(arr[i])
				dp[idx] = arr[i]
			return len(dp)
		result = 0
		for i in range(min(k, len(arr))):
			temp = createNewList(arr, i, k)
			result += len(temp) - getLISwithRepeatedElement(temp)
		return result
        

