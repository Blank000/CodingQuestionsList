
MOD = 10 ** 9 + 7

class Solution:
    def maximumProduct(self, nums: list[int], k: int) -> int:
        nums.sort()
        def get_index():
            for i, n in enumerate(accumulate(nums)):
                if (i + 1) * nums[i] - n >= k:
                    return i
            return len(nums)
        idx = get_index() - 1
        q, r = divmod(k + sum(nums[:idx + 1]), idx + 1)
        return (pow(q + 1, r, MOD) * pow(q, idx + 1 - r, MOD) * prod(nums[idx + 1:])) % MOD