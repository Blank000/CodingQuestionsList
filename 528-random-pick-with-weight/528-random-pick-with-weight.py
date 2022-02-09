import random
import bisect
class Solution:

    def __init__(self, w: List[int]):
        self.footballPitch = w
        for i in range(1, len(self.footballPitch)):
            self.footballPitch[i] += self.footballPitch[i-1] 

    def pickIndex(self) -> int:
        #print(self.footballPitch)
        num = random.randint(1, self.footballPitch[-1])
        idx = bisect.bisect_left(self.footballPitch, num)
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()