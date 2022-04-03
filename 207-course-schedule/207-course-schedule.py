class Solution:
    
    def do_kahn_algo(self, queue, adjList, incoming_degree, numCourses):
        n = 0
        while queue:
            node = queue.pop()
            n += 1
            for neighbour in adjList[node]:
                incoming_degree[neighbour] -= 1
                if incoming_degree[neighbour] == 0:
                    queue.append(neighbour)
        return n == numCourses
                
        
        
            
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = collections.defaultdict(list)
        incoming_degree = collections.defaultdict(int)
        visited = collections.defaultdict(bool)
        for b, a in prerequisites:
            adjList[a].append(b)
            incoming_degree[b] += 1
        queue = []
        for i in range(numCourses):
            if incoming_degree[i] == 0:
                queue.append(i)
        return self.do_kahn_algo(queue, adjList, incoming_degree, numCourses)