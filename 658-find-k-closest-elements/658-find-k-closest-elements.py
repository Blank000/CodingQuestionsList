import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect.bisect_left(arr, x)
        if idx == len(arr):
            return arr[-k:]
        if idx == 0:
            return arr[:k]
        i, j = idx-1, idx
        res = []
        while k:
            if i >= 0 and j < len(arr):
                if abs(x-arr[i]) <= abs(x-arr[j]):
                    res.append(arr[i])
                    i -= 1
                else:
                    res.append(arr[j])
                    j += 1
            elif i >= 0:
                res.append(arr[i])
                i -= 1
            elif j <len(arr):
                res.append(arr[j])
                j += 1
            k -= 1
        return sorted(res)
                