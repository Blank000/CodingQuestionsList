class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        def isDigit(s, idx):
            if ord(s[idx]) >= 48 and ord(s[idx]) <= 57:
                return True
            return False
        def getNum(s, idx):
            if s[idx] == "0":
                return (0, -1)
            res = 0
            oIdx = idx
            while idx < len(s) and isDigit(s, idx):
                res = 10*res + int(s[idx])
                idx += 1
            return (res, idx)
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if not isDigit(abbr, j):
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                res, j = getNum(abbr, j)
                if res == 0:
                    return False
                i += res
        if i == len(word) and j == len(abbr):
            return True
        return False