class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        p = 0
        res = 0
        while n:
            if n&1 == 0:
                res += 2**p
            p += 1
            n >>= 1
        return res