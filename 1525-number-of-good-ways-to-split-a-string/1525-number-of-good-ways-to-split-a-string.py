class Solution:
    def numSplits(self, s: str) -> int:
        leftDistinctDic = [1]*len(s)
        rightDistinctDic = [1]*len(s)
        temp = set()
        numOfGoodSplits = 0
        for i in range(len(s)):
            temp.add(s[i])
            leftDistinctDic[i] = len(temp)
        temp = set()
        for i in range(len(s)-1, -1, -1):
            temp.add(s[i])
            rightDistinctDic[i] = len(temp)
        for i in range(len(s)-1):
            if leftDistinctDic[i] == rightDistinctDic[i+1]:
                numOfGoodSplits += 1
        return numOfGoodSplits