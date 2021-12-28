class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        res = 0
        sign = -1 if (dividend*divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            tempDiv = divisor
            p = 1
            while dividend >= tempDiv:
                dividend -= tempDiv 
                res += p
                p <<= 1
                tempDiv <<= 1
            if sign == 1 and res > 2**31-1:
                return 2**31-1
            if sign == -1 and res > 2**31:
                return -2**31
        return sign*res
            