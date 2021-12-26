class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        x = [1, 0, -1, 0]
        y = [0, 1, 0, -1]
        def check(i, j, n, m):
            # n rows and m cols
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            return True
        dp = [[1 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        maxm = 1
        def getLongestLength(mat, i , j):
            if not check(i, j, len(mat), len(mat[0])):
                return 0
            if dp[i][j] > 1:
                return dp[i][j]
            for d in range(4):
                if check(i+x[d], j+y[d], len(mat), len(mat[0])) and mat[i+x[d]][j+y[d]] < mat[i][j]:
                    l = getLongestLength(mat, i+x[d], j+y[d])
                    dp[i][j] = max(dp[i][j], l+1)
            return dp[i][j]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if dp[i][j] == 1:
                    getLongestLength(mat, i ,j)
                    maxm = max(maxm, dp[i][j])
        return maxm