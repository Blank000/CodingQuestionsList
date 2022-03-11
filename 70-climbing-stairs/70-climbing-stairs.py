class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        d1, d2 = 1, 1
        for i in range(2,n+1):
            d3 = d2
            d4 = d1 + d2
            d1, d2 = d3, d4
        return d4