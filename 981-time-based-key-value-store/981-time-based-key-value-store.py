from sortedcontainers import SortedList
import bisect
class TimeMap:

    def __init__(self):
        self.keyTime = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyTime[key].append([timestamp, value])
            
    def get(self, key: str, timestamp: int) -> str:
        arr = self.keyTime[key]
        low, high = 0, len(arr)
        if high == 0:
            return ""
        while low < high:
            mid = (low+high)//2
            if arr[mid][0] <= timestamp:
                low = mid+1
            else:
                high = mid
        return "" if high == 0 else arr[high-1][1]
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)