class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = {}
        uniqueDiff = set()
        for i in range(len(nums)):
            a = nums[i]
            if (a-k) in dic and (a, a-k) not in uniqueDiff:
                uniqueDiff.add((a-k, a))
            if (k+a) in dic and (a, a+k) not in uniqueDiff:
                uniqueDiff.add((k+a, a))
            dic[a] = 1
        #print(uniqueDiff)
        return len(uniqueDiff)