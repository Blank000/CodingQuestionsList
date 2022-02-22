class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res, p = 0, 0
        for i in range(len(columnTitle)-1, -1, -1):
            c = columnTitle[i]
            res += (26**p)*(ord(c)-65+1)
            p += 1
        return res