class Solution:
    def smallestRepunitDivByK(self, a: int) -> int:
        def getReducedNum(a, b):
            mod = 0
            for i in range(len(b)):
                mod = (mod*10 + int(b[i]))%a
            return mod
        if a == 1:
            return 1
        dic = {}
        b = "1"
        mod = getReducedNum(a, "1")
        counter = 1
        while mod and mod not in dic:
            dic[mod] = 1
            counter += 1
            b = str(mod) + "1"
            #print(b)
            mod = getReducedNum(a, b)
        if mod == 0:
            return counter
        return -1