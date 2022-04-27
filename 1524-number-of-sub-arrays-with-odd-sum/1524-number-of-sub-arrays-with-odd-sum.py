class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9+7
        cumm_sum = 0
        dic = {0:1, 1:0}
        for i in range(len(arr)):
            cumm_sum += arr[i]
            cumm_sum %= 2
            dic[cumm_sum] += 1
        return (dic[0] * dic[1]) % MOD