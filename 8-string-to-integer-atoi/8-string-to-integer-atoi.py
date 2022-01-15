class Solution:
    def myAtoi(self, s: str) -> int:
        idx = 0
        while idx < len(s) and s[idx] == " ":
            idx += 1
        sign = 1
        if idx < len(s) and s[idx] == "-":
            sign = -1
            idx += 1
        elif idx < len(s) and s[idx] == "+":
            idx += 1
        while idx < len(s) and s[idx] == "0":
            idx += 1
        num = ""
        while idx < len(s) and ord(s[idx]) >= 48 and ord(s[idx]) <= 57:
            num += s[idx]
            idx += 1
        res = 0
        p = 0
        for i in range(len(num)-1, -1, -1):
            res = (10**p)*int(num[i]) + res
            p += 1
            if sign == -1 and res >= 2**31:
                return -2**31
            if res > 2**31-1:
                return 2**31-1
        if sign == -1 and res > 2**31:
                return -2**31
        if res > 2**31-1:
            return 2**31-1

        return sign*int(res)