# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        # For each row, do a binary search on cols and find the rightmost column with 1 in it
        rightmostCol = cols
        for k in range(rows):
            i, j = 0, cols-1
            while i <= j:
                mid = (i+j)//2
                val = binaryMatrix.get(k, mid)
                if val == 0:
                    i = mid+1
                else:
                    rightmostCol = min(rightmostCol, mid)
                    j = mid-1
        return -1 if (rightmostCol == cols) else rightmostCol