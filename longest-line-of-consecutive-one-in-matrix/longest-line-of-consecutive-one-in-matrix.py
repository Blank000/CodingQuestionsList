class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        x = [-1, -1, 0, -1]
        y = [1 , -1, -1, 0]
        maxm = 0
        def isValid(mat, i, j):
            if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]):
                return False
            return True
        
        prev = [[0]*4 for _ in range(len(mat[0]))]
        for i in range(len(mat)):
            curr = [[0]*4 for _ in range(len(mat[0]))]
            #curr = [[0]*4 if mat[i][k] == 0 else [1]*4 for k in range(len(mat[i]))]
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    for k in range(4):
                        # Each direction we will explore until we reach end or 0
                        if x[k] != 0 and (j+y[k]) >= 0 and (j+y[k]) < len(mat[0]):
                            curr[j][k] = prev[j+y[k]][k] + 1
                        elif (j+y[k]) >= 0 and (j+y[k]) < len(mat[0]):
                            curr[j][k] = curr[j+y[k]][k] + 1
                        else:
                            curr[j][k] = 1
                        maxm = max(maxm, curr[j][k])
            prev = curr
        return maxm