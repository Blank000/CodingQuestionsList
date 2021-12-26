class Solution:
    def addBinary(self, x: str, y: str) -> str:
        x, y = int(x,2), int(y,2)
        while y:
            x, y = x^y, (x&y) << 1
        return bin(x)[2:]