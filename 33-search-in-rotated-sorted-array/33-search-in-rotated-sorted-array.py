class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def customBinarySearch(arr, start, end, target):
            if start > end:
                return -1
            mid = start + (end - start)//2
            if arr[mid] == target:
                return mid
            if arr[start] <= arr[mid]:
                if target >= arr[start] and target < arr[mid]:
                    return customBinarySearch(arr, start, mid-1, target)
                else:
                    return customBinarySearch(arr, mid+1, end, target)
            else:
                if target > arr[mid] and target <= arr[end]:
                    return customBinarySearch(arr, mid+1, end, target)
                else:
                    return customBinarySearch(arr, start, mid-1, target)
        return customBinarySearch(nums, 0, len(nums)-1, target)