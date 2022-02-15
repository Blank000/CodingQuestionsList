import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points
        distn = list(map(lambda x: [x[1][0]**2+x[1][1]**2, x[0]], enumerate(points)))
        def quickSelect(distn, start, end):
            if start >= end:
                return False
            idx = shiftAllSmallerToPivotOnLeft(distn, start, end)
            if idx == k-1:
                return True
            if idx < k:
                return quickSelect(distn, idx+1, end)
            return quickSelect(distn, start, idx-1)
        
            
        def shiftAllSmallerToPivotOnLeft(distn, start, end):
            pivotDistn, idx = distn[end]
            i = start
            for j in range(start, end):
                d, idx = distn[j]
                if d <= pivotDistn:
                    distn[j], distn[i] = distn[i], distn[j]
                    i += 1
            distn[i], distn[end] = distn[end], distn[i]
            return i
        quickSelect(distn, 0, len(distn)-1)
        #print(distn)
        return [points[distn[i][1]] for i in range(k)]
            
        