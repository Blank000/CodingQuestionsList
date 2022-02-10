class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        dic = {}
        dic[0] = 1
        res = 0
        for i in range(len(nums)):
            if (nums[i]-k) in dic:
                res += dic[nums[i]-k]
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        
        return res
                