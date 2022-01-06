import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Here are this thing needs to be checked, that 
        # number of passangers at anypoint of time must not exceed the capacity
        l = []
        for i in range(len(trips)):
            l.append([trips[i][1], trips[i][0]])
            l.append([trips[i][2], -trips[i][0]])
        l.sort()
        curr = 0
        for t, c in l:
            curr += c
            if curr > capacity:
                return False
        return True