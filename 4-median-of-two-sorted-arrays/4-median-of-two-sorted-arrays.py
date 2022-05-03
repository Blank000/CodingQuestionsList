import bisect
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        # I will choose a element and try to make it as a median
        # Median is all about being in middle
        # There are two cases, one with odd number of elements and one with the even number of elements
        if len(A) > len(B):
            return self.findMedianSortedArrays(B, A)
        n1, n2 = len(A), len(B)
        low, high = 0, len(A)
        while low <= high:
            mid1 = low + (high - low)//2
            mid2 = (n1+n2)//2 - mid1
            l1 = -math.inf if mid1 <= 0 else A[mid1-1]
            r1 = math.inf if mid1 >= len(A) else A[mid1]
            l2 = -math.inf if mid2 <= 0 else B[mid2-1]
            r2 = math.inf if mid2 >= len(B) else B[mid2]
            #print(low, l1, l2, r1, r2)
            if l1 > r2:
                high = mid1
            elif l2 > r1:
                low = mid1 + 1
            else:
                #print(low, l1, l2, r1, r2)
                if (n1 + n2) % 2 != 0:
                    return min(r1, r2)
                return (max(l1, l2) + min(r1, r2)) / 2
#        print(low)
        return -1