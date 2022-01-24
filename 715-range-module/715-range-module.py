import heapq
class RangeModule:

    def __init__(self):
        self.time = []

    def addRange(self, left: int, right: int) -> None:
        # first gets the leftmost insertion index of the left value and the rightmost insertion index of the right value. Then, we check if either of these indexes are even. If the index is even, it means that it is currently outside the range of start and end indexes being tracked. In this case, we include this index to be updated in the tracking array. We then use python array slicing to overwrite the tracking array with the left and right values placed in the correct index
        lIdx, rIdx = bisect.bisect_left(self.time, left), bisect.bisect_right(self.time, right)
        # If the indexes are even then that mean the number is there but if it's odd then it doesn't
        self.time[lIdx:rIdx] = [left]*(lIdx&1 == 0) + [right]*(rIdx&1 == 0)


    def queryRange(self, left: int, right: int) -> bool:
        # gets the rightmost insertion index of the left value and the leftmost insertion index of the right value. If both these indexes are equal and these indexes are odd, it means the range queried is inside the range of values being tracked. In this case, we return True. Else, we return False
        lIdx, rIdx = bisect.bisect_right(self.time, left), bisect.bisect_left(self.time, right)
        if lIdx&1 != 0 and lIdx == rIdx:
            return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        # first gets the leftmost insertion index of the left value and the rightmost insertion index of the right value. Then, we check if either of these indexes are odd. If the index is odd, it means that it is currently inside the range of start and end indexes being tracked. In this case, we include this index to be updated in the tracking array. We then use python array slicing to overwrite the tracking array with the left and right values placed in the correct index. 
        lIdx, rIdx = bisect.bisect_left(self.time, left), bisect.bisect_right(self.time, right)
        self.time[lIdx:rIdx] = [left]*(lIdx&1 != 0) + [right]*(rIdx&1 != 0)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)