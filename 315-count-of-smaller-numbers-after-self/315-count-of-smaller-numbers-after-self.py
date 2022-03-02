class Solution:
	def countSmaller(self, nums: List[int]) -> List[int]:
		smallCount = [0]*len(nums)
		def mergeSort(nums, start, end):
			if start >= end:
				return
			mid = start + (end-start)//2
			mergeSort(nums, start, mid)
			mergeSort(nums, mid+1, end)
			merge(nums, start, mid, end)
		def merge(nums, start, mid, end):
			temp = []
			i, j = start, mid+1
			while i <= mid:
				while i <= mid and j <= end and nums[j][0] < nums[i][0]:
					temp.append((nums[j][0],nums[j][1]))
					j += 1
				smallCount[nums[i][1]] += j-mid-1
				temp.append((nums[i][0], nums[i][1]))
				i += 1
			while j <= end:
				temp.append((nums[j][0], nums[j][1]))
				j += 1
			for i in range(len(temp)):
				nums[i+start] = temp[i]
		for i in range(len(nums)):
			nums[i] = (nums[i], i)
		print(nums)
		mergeSort(nums, 0, len(nums)-1)
		
		return smallCount

