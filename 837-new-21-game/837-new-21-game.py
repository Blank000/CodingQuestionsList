class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # think in a forward but code in reverse way. So when you are at ith position then you can go to i+1 to i+maxPts position from there. Now if you think in reverse manner then to reach a pth position , you can reach from (p-1)th , (p-2)th ...... (p-maxPts)th position , so the number of ways => numberOfWays[p-1] + numberOfWays[p-2] ....... + numberOfWays[p-maxPts] and to get a certain number from the range of [1, maxPts], the probability is 1/maxPts
        # To get from ith to pth position in one go, the probability becomes => probabilityToReach[i] * 1/maxPts and considering this we get the final formulae as probabilityToReach[p] = sum(probabilityToReach[j] where j < p and j >= 0 and if p >= m you also have to remove the probabilty from the start)
        if k == 0 or n >= k+maxPts:
            return 1
        probabilityToReach = [0]*(n+1)
        probabilityToReach[0] = 1
        probabilitySummation = 1
        for i in range(1, n+1):
            probabilityToReach[i] = probabilitySummation/maxPts
            if i >= maxPts:
                probabilitySummation -= probabilityToReach[i-maxPts]
            if i < k:
                probabilitySummation += probabilityToReach[i]
        return sum(probabilityToReach[k:n+1])
        