class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def binarySearch(arr, start, end):
            if start >= end:
                return arr[start]
            mid = start + (end - start)//2
            if mid&1 == 0:
                if arr[mid] == arr[mid+1]:
                    return binarySearch(arr, mid+1, end)
                else:
                    return binarySearch(arr, start, mid)
            else:
                if arr[mid] == arr[mid-1]:
                    return binarySearch(arr, mid+1, end)
                else:
                    return binarySearch(arr, start, mid)
        return binarySearch(nums, 0, len(nums)-1)
            