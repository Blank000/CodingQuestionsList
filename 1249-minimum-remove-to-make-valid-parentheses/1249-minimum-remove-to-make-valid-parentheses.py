class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l = list(s)
        count = 0
        for i in range(len(s)):
            if l[i] == ")":
                if count == 0:
                    l[i] = ""
                else:
                    count -= 1
            elif l[i] == "(":
                count += 1
        count = 0
        for i in range(len(s)-1, -1, -1):
            if l[i] == "(":
                if count == 0:
                    l[i] = ""
                else:
                    count -= 1
            elif l[i] == ")":
                count += 1
        return "".join(l)
            