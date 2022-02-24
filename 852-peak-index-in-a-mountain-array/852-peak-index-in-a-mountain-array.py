class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, h = 0, len(arr)-1
        while l < h:
            mid = l + ((h-l)>>1)
            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return mid
            if arr[mid] > arr[mid+1] and arr[mid-1] > arr[mid]:
                h = mid - 1
            else:
                l = mid + 1
        return l