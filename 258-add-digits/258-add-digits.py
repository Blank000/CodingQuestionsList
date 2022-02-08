class Solution:
    def addDigits(self, num: int) -> int:
        def digitSum(num):
            res = 0
            while num:
                res += num%10
                num //= 10
            return res
        while num >= 10:
            num = digitSum(num)
        return num