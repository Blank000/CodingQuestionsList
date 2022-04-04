from collections import defaultdict
class Solution:
    
    def do_dfs(self, vertex, adjList, visited, is_stack, topological_order):
        visited[vertex] = True
        is_stack[vertex] = True
        for neighbor in adjList[vertex]:
            if not visited[neighbor]:
                if not self.do_dfs(neighbor, adjList, visited, is_stack, topological_order):
                    return False
            elif is_stack[neighbor]:
                return False
        topological_order.append(vertex)
        is_stack[vertex] = False
        return True
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for b,a in prerequisites:
            adjList[a].append(b)
        visited = defaultdict(bool)
        is_stack = defaultdict(bool)
        topological_order = []
        for vertex in range(numCourses):
            if not visited[vertex]:
                if not self.do_dfs(vertex, adjList, visited, is_stack, topological_order):
                    return []
        return topological_order[::-1]
        
        