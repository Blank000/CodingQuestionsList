class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        firstNum = 1
        for i in range(len(arr)):
            n = arr[i]
            
            diff = n-firstNum
            if k <= diff:
                return firstNum+k-1
            else:
                k -= diff
            if diff > 0:
                firstNum = arr[i]+1
            else:
                firstNum += 1
        return firstNum+k-1
                