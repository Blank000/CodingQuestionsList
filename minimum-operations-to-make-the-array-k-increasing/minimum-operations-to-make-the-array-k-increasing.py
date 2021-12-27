import bisect
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        # Make array with each element that are k seperated from a certain index and then add the number of changes to be made
        
        def createKArr(arr, idx, temp, k):
            while idx < len(arr):
                temp.append(arr[idx])
                arr[idx] = -1
                idx += k
        
        def getLis(arr):
            count = 0
            dp = []
            for i in range(len(arr)):
                idx = bisect.bisect_right(dp, arr[i])
                if idx == len(dp):
                    dp.append(arr[i])
                else:
                    dp[idx] = arr[i]
            return len(dp)
            
        res = 0
        for i in range(len(arr)):
            if arr[i] != -1:
                temp = []
                createKArr(arr, i, temp, k)
                print(temp)
                res += len(temp) - getLis(temp)
        return res
    
    