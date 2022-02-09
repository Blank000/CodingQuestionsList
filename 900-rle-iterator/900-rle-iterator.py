class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.remainingCount = 0
        self.remainingNum = -1
        self.idx = 0
        self.encoding = encoding

    def next(self, n: int) -> int:
        val = -1
        p = n
        while n:
            if self.idx >= len(self.encoding) and self.remainingCount < n:
                self.remainingCount = 0
                self.remainingNum = -1
                return -1
            if self.remainingCount > 0:
                if self.remainingCount >= n:
                    self.remainingCount -= n
                    return self.remainingNum
                else:
                    n -= self.remainingCount
                    self.remainingCount = 0
                    self.remainingNum = -1
            m = self.encoding[self.idx]
            val = self.encoding[self.idx + 1]
            if m >= n:
                self.remainingCount = m-n
                self.remainingNum = val
                self.idx += 2
                return val
            else:
                self.idx += 2
                n -= m
                


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)