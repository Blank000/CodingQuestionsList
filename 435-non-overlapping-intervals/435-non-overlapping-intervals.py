class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        minEnd = float("-inf")
        res = 0
        currOverlap = 1
        intervals.sort()
        for start, end in intervals:
            if start >= minEnd:
                minEnd = end
                res += currOverlap - 1
                currOverlap = 1
            else:
                minEnd = min(minEnd, end)
                currOverlap += 1
        return res + currOverlap - 1
                