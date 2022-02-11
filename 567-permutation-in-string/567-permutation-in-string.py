class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        substrDic = collections.defaultdict(int)
        for i in range(len(s1)):
            substrDic[s1[i]] += 1
        slidingWindow = collections.defaultdict(int)
        for i in range(len(s1)):
            slidingWindow[s2[i]] += 1 
        if slidingWindow == substrDic:
            return True
        for i in range(len(s1), len(s2)):
            slidingWindow[s2[i]] += 1 
            slidingWindow[s2[i-len(s1)]] -= 1 
            if slidingWindow[s2[i-len(s1)]] == 0:
                del slidingWindow[s2[i-len(s1)]]
            if slidingWindow == substrDic:
                return True
        return False
            