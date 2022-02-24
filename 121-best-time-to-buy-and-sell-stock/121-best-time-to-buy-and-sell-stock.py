class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minm = float("inf")
        profit = 0
        for p in prices:
            minm = min(minm, p)
            profit = max(profit, p-minm)
        return profit