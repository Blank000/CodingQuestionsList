class Solution:
    def addDigits(self, n: int) -> int:
        if n == 0:
            return 0
        return 9 if n%9 == 0 else n%9