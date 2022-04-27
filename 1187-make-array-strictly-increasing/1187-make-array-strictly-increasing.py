import bisect
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        @lru_cache(None)
        def getNumberOfOperations(i, prev_value):
            if i == len(arr1):
                return 0
            count = math.inf
            idx = bisect.bisect_right(arr2 , prev_value)
            if idx == len(arr2):
                if arr1[i] <= prev_value:
                    return math.inf
                else:
                    count = min(count, getNumberOfOperations(i+1, arr1[i]))
            else:
                if arr1[i] <= prev_value:
                    count = min(count, 1+getNumberOfOperations(i+1, arr2[idx]))
                else:
                    count = min(count, min(getNumberOfOperations(i+1, arr1[i]), 1+getNumberOfOperations(i+1, arr2[idx])))
            return count
        count = getNumberOfOperations(0, -1)
        return count if count != math.inf else -1