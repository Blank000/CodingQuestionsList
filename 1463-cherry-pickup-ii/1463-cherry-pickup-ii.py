class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # Bottom up approach 
        # dp[k][i][j] donotes if the two robots start from grid[k][i] and grid[k][j] the maximum total 
        # cherries they can pickup at last. Note they can only move downstairs.
        # After we fulfill dp, the final answer is dp[0][0][COL_NUM - 1]
        def isValid(i, grid):
            if i < 0 or i >= len(grid[0]):
                return False
            return True
        dp = [[[0]*len(grid[0]) for _ in range(len(grid[0]))] for _ in range(len(grid))]
        #print(dp)
        for k in range(len(grid)-1, -1, -1):
            for i in range(len(grid[0])):
                for j in range(len(grid[0])):
                    if k == len(grid) - 1:
                        dp[k][i][j] = grid[k][i] if i == j else (grid[k][i] + grid[k][j])
                    else:
                        for di in (-1, 0, 1):
                            for dj in (-1, 0, 1):
                                if isValid(i+di, grid) and isValid(j+dj, grid):
                                    if i == j:
                                        dp[k][i][j] = max(dp[k][i][j], dp[k+1][i+di][j+dj] + grid[k][i])
                                    else:
                                        #print(i,j,di,dj,k,dp[k+1][i+di][j+dj])
                                        dp[k][i][j] = max(dp[k][i][j], dp[k+1][i+di][j+dj] + grid[k][i] + grid[k][j])
        return dp[0][0][len(grid[0])-1]
                