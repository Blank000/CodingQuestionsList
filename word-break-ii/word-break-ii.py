from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # So basically the below dictionary is storing the words that can be created ahead of a certain breakpoint index
        dic = defaultdict(set)
        breakpoints = [0]
        for i in range(len(s)):
            for j in breakpoints:
                if s[j:i+1] in wordDict:
                    breakpoints.append(i+1)
                    # Whichever words are starting froma. certain breakpoint up to a certain index
                    dic[j].add(s[j:i+1])
        res = []
        def createList(idx, temp, s):
            if idx == len(s):
                res.append(" ".join(temp))
                return
            if idx in breakpoints:
                for c in dic[idx]:
                    createList(idx + len(c), temp+[c], s)
        createList(0, [], s)
        return res
                    