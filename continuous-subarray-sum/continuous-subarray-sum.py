class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
         This concept is really unique where lets say we have created a prefix array and then 
         prefix[j] - prefix[i] = d and d%k = 0 then prefix[i]%k = prefix[j]%k, now the same thing we are
         gonna check here that if a mod repeats then we have a subarray whose sum is divisble by k
        '''
        if len(nums) == 1:
            return False
        if len(nums) == 2:
            if sum(nums)%k == 0:
                return True
            return False
        dic = {}
        mod = nums[0]%k
        dic[mod] = 0
        dic[0] = -1
        for i in range(1,len(nums)):
            mod = (mod+nums[i])%k
            if mod in dic and i-dic[mod]> 1:
                return True
            if mod not in dic:
                dic[mod] = i
        return False
        