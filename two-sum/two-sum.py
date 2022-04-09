class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            k = target-nums[i]
            if k in dic:
                return [i, dic[k][1]]
            dic[nums[i]] = [k, i]
            