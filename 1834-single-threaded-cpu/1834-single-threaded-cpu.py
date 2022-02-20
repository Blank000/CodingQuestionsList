import heapq
class Solution:
        
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,v in enumerate(tasks):
            v.append(i)
        tasks.sort()
        time = tasks[0][0]
        heap = []
        heapq.heappush(heap, (tasks[0][1], tasks[0][2]))
        res = []
        i = 1
        while i < len(tasks) or heap:
            #print(time,heap,tasks,tasks[i][0])
            timeToComplete, idx = heapq.heappop(heap)
            time += timeToComplete
            res.append(idx)
            while i < len(tasks) and tasks[i][0] <= time:
                #print(heap, time, tasks[i])
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if len(heap) == 0 and i < len(tasks):
                time = tasks[i][0]
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                
                i += 1
            #print(heap, time, tasks[i])
        return res