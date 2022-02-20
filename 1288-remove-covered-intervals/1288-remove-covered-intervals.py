import bisect
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: [x[0], -x[1]])
        covered = 1
        start, end = intervals[0][0], intervals[0][1]
        for i in range(1,len(intervals)):
            s,e = intervals[i]
            if s >= start and e <= end:
                covered -= 1
            start = min(start, s)
            end = max(end, e)
            covered += 1
        return covered