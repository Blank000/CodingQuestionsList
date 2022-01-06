class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        x = [1, -1, 0, 0]
        y = [0, 0, 1, -1]
        
        def isValid(i,j):
            if i <0 or j <0 or i>= len(grid) or j >= len(grid[0]):
                return False
            return True
        def dfs(grid, i, j):
            if not isValid(i,j) or grid[i][j] == 0:
                return 0
            v = 1
            grid[i][j] = 0
            for d in range(4):
                v += dfs(grid, i+x[d], j+y[d])
            return v
                    
        maxmArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxmArea = max(maxmArea, dfs(grid, i, j))
                    #print(maxmArea , i, j)
        return maxmArea
        
                    
            