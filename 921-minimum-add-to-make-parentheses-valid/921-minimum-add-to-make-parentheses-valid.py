class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = 0
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                n += 1
            else:
                if n == 0:
                    res += 1
                else:
                    n -= 1
        return res + n