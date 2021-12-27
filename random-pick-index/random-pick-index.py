class Solution:

    def __init__(self, nums: List[int]):
        self.dic = collections.defaultdict(list)
        self.nums = nums

    def pick(self, target: int) -> int:
        if target in self.dic:
            return random.choice(self.dic[target])
        arr = []
        for i,n in enumerate(self.nums):
            if n == target:
                arr.append(i)
        self.dic[target] = arr
        return random.choice(arr)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)