from sortedcontainers import SortedList
class MyCalendarThree:

    def __init__(self):
        self.intervals = SortedList()

    def book(self, start: int, end: int) -> int:
        self.intervals.add((start, end))
        numOfConfRoomReqd = float("-inf")
        currOverlappingIntervals = 1
        endList = []
        heapq.heapify(endList)
        for start, end in self.intervals:
            count = 0
            currOverlappingIntervals += 1
            if not endList:
                currOverlappingIntervals = 1
            elif endList[0] <= start:
                currOverlappingIntervals -= 1
                heapq.heappop(endList)
            
            heapq.heappush(endList, end)
            numOfConfRoomReqd = max(numOfConfRoomReqd, currOverlappingIntervals)
        return numOfConfRoomReqd


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)