class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        componentNumber = 1
        componentDic = {}
        componentDic[0] = 0
        def dfs(grid, i, j, itr, visited):
            if grid[i][j] == 0 or (i,j) in visited:
                return
            visited[(i,j)] = True
            itr.append((i,j))
            if i+1 < len(grid):
                dfs(grid, i+1, j, itr, visited)
            if j+1 < len(grid[0]):
                dfs(grid, i, j+1, itr, visited)
            if i-1 >= 0:
                dfs(grid, i-1, j, itr, visited)
            if j-1 >= 0:
                dfs(grid, i, j-1, itr, visited)
        visited = collections.defaultdict(bool)
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    itr = []
                    dfs(grid, i, j, itr, visited)
                    #print(visited, itr)
                    area = len(itr)
                    maxArea = max(maxArea, area)
                    for p,q in itr:
                        grid[p][q] = componentNumber
                    componentDic[componentNumber] = area
                    componentNumber += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    componentSet = set()
                    if i+1 < len(grid):
                        componentSet.add(grid[i+1][j])
                    if j+1 < len(grid[0]):
                        componentSet.add(grid[i][j+1])
                    if i-1 >= 0:
                        componentSet.add(grid[i-1][j])
                    if j-1 >= 0:
                        componentSet.add(grid[i][j-1])
                    area = 1
                    for s in componentSet:
                        area += componentDic[s]
                    maxArea = max(maxArea, area)
        return maxArea
                    