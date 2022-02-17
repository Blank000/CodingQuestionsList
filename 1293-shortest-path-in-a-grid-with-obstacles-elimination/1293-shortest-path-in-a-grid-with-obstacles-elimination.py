class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        dic = {}
        dic[(0,0)] = k-1 if grid[0][0] == 1 else k
        visited = {(0,0):1}
        x = [1, -1, 0, 0]
        y = [0, 0, 1, -1]
        def isGood(a,b,grid):
            if a <0 or b <0 or a >= len(grid) or b >= len(grid[0]):
                return False
            return True
        def bfs(dic, visited, grid, level, x, y):
            tempDic = {}
            if len(dic) == 0:
                return -1
            for key,v in dic.items():
                i, j = key
                if i == len(grid)-1 and j == len(grid[0])-1:
                    return level-1
                for l in range(4):
                    a, b = i+x[l] , j+y[l]
                    
                    if isGood(a,b,grid) and ((a,b) not in visited or visited[(a, b)] < v) and (grid[a][b] == 0 or (grid[a][b] == 1 and v > 0)):
                        value = v-1 if grid[a][b] == 1 else v
                        tempDic[(a,b)] = value if (a,b) not in tempDic else max(value, tempDic[(a,b)])
            for k,v in tempDic.items():
                visited[(k[0], k[1])] = v
            #print(tempDic)
            return bfs(tempDic, visited, grid, level+1, x, y)
        return bfs(dic, visited, grid, 1, x, y)