class Solution:
    def __init__(self):
        self.itr = 1
    def dfs(self, grid, i, j, x, y):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
            return True
        
        if grid[i][j] > 0:
            return False
        val = False
        grid[i][j] = self.itr
        if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[0])-1:
            val = True
        for k in range(4):
            val = self.dfs(grid, i+x[k], j+y[k], x, y) or val
        
        return val
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        x = [1, -1, 0, 0]
        y = [0, 0, 1, -1]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    if not self.dfs(grid, i, j, x, y):
                        
                        self.itr += 1
        return self.itr-1
            