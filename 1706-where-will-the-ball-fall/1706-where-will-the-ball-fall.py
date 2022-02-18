class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def traverse(ballLocn, grid):
            x, y = ballLocn
            l = grid[x][y]
            if x== -1 or y == -1:
                return -1
            if x == len(grid)-1 :
                if y+l >= 0 and y+l < len(grid[0]) and grid[x][y+l] == l:
                    return y+l
                else:
                    return -1
            #print(x, y, l, grid[x][y], grid[x][y+l])
            if y+l < len(grid[0]) and y+l >= 0 and grid[x][y+l] == l:
                ballLocn = [x+1, y+l]
            else:
                return -1
            return traverse(ballLocn, grid)
                    
                
        res = []
        for j in range(len(grid[0])):
            ballLocn = [0, j]
            idx = traverse(ballLocn, grid)
            res.append(idx)
        return res