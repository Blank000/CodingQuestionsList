from collections import defaultdict
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N == 1:
            return 1
        if len(trust) == 0:
            return -1
        graph = defaultdict(list)
        for v in trust:
            graph[v[0]].append(v[1])
        count = 0
        res = -1
        for p in range(1,N+1):
            if p not in graph:
                for k in graph:
                    if not p in graph[k]:
                        return -1
                count += 1
                res = p
        if count == 1:
            return res
        return -1