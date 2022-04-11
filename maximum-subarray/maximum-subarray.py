class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefixSumm = [0]
        summ = 0
        for n in nums:
            summ += n
            prefixSumm.append(summ)
        minm = math.inf
        sumMax = -math.inf
        for p in prefixSumm:
            sumMax = max(sumMax, p-minm)
            minm = min(minm, p)
        return sumMax
            