class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        dic = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in dic:
                    area = 0
                    st = [(i, j)]
                    dic[(i, j)] = 1
                    while st:
                        x, y = st.pop()
                        area += 1
                        if (0 <= (x-1) < len(grid)) and grid[x-1][y] != 0 and (x-1, y) not in dic: 
                            st.append((x-1, y))
                            dic[(x-1, y)] = 1
                        if (0 <= (x+1) < len(grid)) and grid[x+1][y] != 0 and (x+1, y) not in dic: 
                            st.append((x+1, y))
                            dic[(x+1, y)] = 1
                        if (0 <= (y-1) < len(grid[0])) and grid[x][y-1] != 0 and (x, y-1) not in dic: 
                            st.append((x, y-1))
                            dic[(x, y-1)] = 1
                        if (0 <= (y+1) < len(grid[0])) and grid[x][y+1] != 0 and (x, y+1) not in dic: 
                            st.append((x, y+1))
                            dic[(x, y+1)] = 1

                    ans = max(ans, area)
        return ans
