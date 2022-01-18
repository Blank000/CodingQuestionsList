import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        numOfConfRoomReqd = float("-inf")
        currOverlappingIntervals = 1
        endList = []
        heapq.heapify(endList)
        for start, end in intervals:
            count = 0
            if not endList:
                currOverlappingIntervals = 1
            elif endList[0] <= start:
                #currOverlappingIntervals -= 1
                heapq.heappop(endList)
            else:
                currOverlappingIntervals += 1
            heapq.heappush(endList, end)
            numOfConfRoomReqd = max(numOfConfRoomReqd, currOverlappingIntervals)
        return numOfConfRoomReqd
                