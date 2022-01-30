import bisect
class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> bool:
        if len(self.arr) == 0:
            self.arr.append(start)
            self.arr.append(end)
            return True
        else:
            startIdx = bisect.bisect_right(self.arr, start)
            endIdx = bisect.bisect_left(self.arr, end)
            #print(startIdx, endIdx)
            if startIdx & 1 == 0 and endIdx & 1 == 0 and startIdx == endIdx:
                self.arr[startIdx:endIdx] = [start, end]
                return True
            return False
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)