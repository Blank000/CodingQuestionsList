class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # https://youtu.be/HsY3jFyaePU
        # Recursive solution 
        def recurse(stoneValue, i, dp):
            if i >= len(stoneValue):
                return 0
            if dp[i]:
                return dp[i]
            ans = float("-inf")
            ans = max(ans, stoneValue[i] - recurse(stoneValue, i+1, dp))
            if i+1 < len(stoneValue):
                ans = max(ans, stoneValue[i+1] + stoneValue[i] - recurse(stoneValue, i+2, dp))
            if i+2 < len(stoneValue):
                ans = max(ans, stoneValue[i+2] + stoneValue[i+1] + stoneValue[i]- recurse(stoneValue, i+3, dp))
            dp[i] = ans
            return ans
        dp = [0]*len(stoneValue)
        val = recurse(stoneValue, 0, dp)
        if val < 0:
            return "Bob"
        if val == 0:
            return "Tie"
        return "Alice"