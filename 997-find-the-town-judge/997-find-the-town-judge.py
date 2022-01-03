class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dic = collections.defaultdict(set)
        for t in trust:
            dic[t[0]].add(t[1])
        
        res = -1
        for i in range(n):
            if (i+1) not in dic:
                if res != -1:
                    return -1
                res = i+1
        if res == -1:
            return -1
        for k, v in dic.items():
            if res not in v:
                return -1
        return res
            