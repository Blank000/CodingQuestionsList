from collections import defaultdict
class Solution:
    def do_dfs(self, vertex, adjList, visited, is_present_in_recursion_stack, order):
        visited[vertex] = True
        is_present_in_recursion_stack[vertex] = True
        for neighbour in adjList[vertex]:
            if not visited[neighbour]:
                if not self.do_dfs(neighbour, adjList, visited, is_present_in_recursion_stack, order):
                    return False
            elif is_present_in_recursion_stack[neighbour]:
                return False
        is_present_in_recursion_stack[vertex] = False
        order.append(vertex)
        return True
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        visited = defaultdict(bool)
        is_present_in_recursion_stack = defaultdict(bool)
        for b,a in prerequisites:
            adjList[a].append(b)
        order = []
        for i in range(numCourses):
            if not visited[i]:
                if not self.do_dfs(i, adjList, visited, is_present_in_recursion_stack, order):
                    return []
        return order[::-1]
        
            