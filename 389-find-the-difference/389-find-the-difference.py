class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = collections.defaultdict(int)
        for i in range(len(s)):
            dic[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in dic:
                return t[i]
            dic[t[i]] -= 1
            if dic[t[i]] == 0:
                del dic[t[i]]
        for k in dic.keys():
            return k
            