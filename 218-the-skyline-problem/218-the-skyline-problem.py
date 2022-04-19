class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def comparator(element):
            if element[2] == "S":
                return (element[0], -element[1])
            return (element[0], element[1])
                
        intervals = []
        for left, right, height in buildings:
            intervals.append([left, height, "S"])
            intervals.append([right, height, "E"])
        intervals.sort(key = comparator)
        #print(intervals)
        heap = [0]
        heapq.heapify(heap)
        ans = []
        previousMaxHeight = 0
        for x, y, d in intervals:
            if d == "S":
                heapq.heappush(heap, -y)
            else:
                heap.remove(-y)
                heapq.heapify(heap)
            if previousMaxHeight != -heap[0]:
                ans.append([x, -heap[0]])
                previousMaxHeight = -heap[0]
        return ans

    
    
    

                