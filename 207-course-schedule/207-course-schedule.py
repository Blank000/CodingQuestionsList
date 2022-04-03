class Solution:
    
    def do_dfs(self, vertex, adjList, visited, is_present_in_recursion_stack):
        visited[vertex] = True
        is_present_in_recursion_stack[vertex] = True
        for neighbour in adjList[vertex]:
            if not visited[neighbour]:
                if not self.do_dfs(neighbour, adjList, visited, is_present_in_recursion_stack):
                    return False
            elif is_present_in_recursion_stack[neighbour]:
                return False
        is_present_in_recursion_stack[vertex] = False
        return True
        
            
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = collections.defaultdict(list)
        visited = collections.defaultdict(bool)
        is_present_in_recursion_stack = collections.defaultdict(bool)
        for b, a in prerequisites:
            adjList[a].append(b)
        # Will be doing dfs to find a back edge, as we don't know , there can be a graph forest, so I will be maintaing both visited and is_present_in_stack
        for i in range(numCourses):
            if not visited[i]:
                if not self.do_dfs(i, adjList, visited, is_present_in_recursion_stack):
                    return False
        return True
    
        