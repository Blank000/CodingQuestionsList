class Solution:
    def findComplement(self, num: int) -> int:
        p = 0
        res = 0
        while num:
            if not(1 & num):
                res += 2**p
            p += 1
            num >>= 1
        return res
                