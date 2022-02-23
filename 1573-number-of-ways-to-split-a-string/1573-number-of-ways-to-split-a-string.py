class Solution:
    def numWays(self, s: str) -> int:
        oneIdx = []
        for i in range(len(s)):
            if s[i] == "1":
                oneIdx.append(i)
        if len(oneIdx)%3 != 0:
            return 0
        if len(oneIdx) == 0:
            n = len(s)-2
            return (n*(n+1)//2)%(10**9+7)
        idx = len(oneIdx)//3
        lastIdx = len(oneIdx) - len(oneIdx)//3
        return ((oneIdx[idx] - oneIdx[idx-1]) * (oneIdx[lastIdx] - oneIdx[lastIdx-1]))%(10**9+7)