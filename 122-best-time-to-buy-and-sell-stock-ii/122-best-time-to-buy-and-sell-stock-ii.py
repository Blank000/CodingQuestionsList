class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minm = prices[0]
        for i in range(1,len(prices)):
            if prices[i] > minm:
                profit += prices[i] - minm
                minm = prices[i]
            else:
                minm = prices[i]
        return profit