from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        res = 0
        for x in counter:
            if x+k in counter and k > 0:
                res += 1
            elif k == 0 and counter[x] > 1:
                res += 1
        return res