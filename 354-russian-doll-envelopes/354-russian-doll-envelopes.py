class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = list(map(lambda x: (x[0], x[1]), envelopes))
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        heights = [x[1] for x in envelopes]
        # Now it's a standard LIS wuestion
        dp = []
        for i in range(len(heights)):
            idx = bisect.bisect_left(dp, heights[i])
            if idx == len(dp):
                dp.append(heights[i])
            else:
                dp[idx] = heights[i]
        return len(dp)
        