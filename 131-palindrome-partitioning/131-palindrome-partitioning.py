class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # This question can be solved using gap interval technique or even the breakpoint technique
        breakpoints = collections.defaultdict(list)
        for i in range(len(s)):
            breakpoints[i] = []
        def getListOfPallindromes(breakpoints, s):
            for i in range(len(s)):
                for b,v in breakpoints.items():
                    if b > i:
                        break
                    if s[b:i+1] == s[b:i+1][::-1]:
                        breakpoints[b].append(s[b:i+1])
        getListOfPallindromes(breakpoints, s)
        res = []
        def addPallindromeSubsets(res, breakpoints, idx, s, tempArr):
            if idx == len(s):
                res.append(tempArr[::])
                return
            for word in breakpoints[idx]:
                tempArr.append(word)
                addPallindromeSubsets(res, breakpoints, idx+len(word), s, tempArr)
                tempArr.pop()
        addPallindromeSubsets(res, breakpoints, 0, s, [])
        return res