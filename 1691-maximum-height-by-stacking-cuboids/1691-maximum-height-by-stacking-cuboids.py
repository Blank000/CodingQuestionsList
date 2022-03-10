class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for c in cuboids:
            c.sort()
        cuboids.sort()
        dp = [c[2] for c in cuboids]
        for i in range(len(dp)):
            for j in range(i):
                if cuboids[j][0] <= cuboids[i][0] and cuboids[j][1] <= cuboids[i][1] and cuboids[j][2] <= cuboids[i][2]:
                    dp[i] = max(dp[i], cuboids[i][2] + dp[j])
        return max(dp)
                    