import heapq
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # This can be solved using binary search. Here we need the number of pops <= h
        def getNumberOfPops(piles, k):
            numberOfPops = 0
            for p in piles:
                numberOfPops += math.ceil(p/k)
            return numberOfPops
        start, end = 1, max(piles)
        while start < end:
            mid = start + (end - start)//2
            noOfPops = getNumberOfPops(piles, mid)
            if noOfPops <= h:
                end = mid
            else:
                start = mid+1
        return end
            
            