class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        idx = []
        for i,s in enumerate(seats):
            if s == 1:
                idx.append(i)
        maxm = max(idx[0], len(seats)-idx[-1]-1)
        for i in range(1,len(idx)):
            maxm = max(maxm, (idx[i] - idx[i-1])//2)
        return maxm