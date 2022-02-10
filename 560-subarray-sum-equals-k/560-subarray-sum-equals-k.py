class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # This is the question where we will use the dictionary approach of prefix sum array
        dic = collections.defaultdict(int)
        ps = 0
        count = 0
        dic[0] = 1
        for n in nums:
            ps += n
            if (ps-k) in dic:
                count += dic[ps-k]
            dic[ps] += 1
        return count
                