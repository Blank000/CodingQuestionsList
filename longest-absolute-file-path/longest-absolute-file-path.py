class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maxLen = 0
        currLen = 0
        st = []
        arr = input.split("\n")
        for a in arr:
            t = a.split("\t")
            isFile = False
            if len(t) == 1:
                st = []
                st.append(a)
                currLen = len(a)
                if a.count(".") > 0:
                    isFile = True
            else:
                while st and len(st) >= len(t):
                    e = st.pop()
                    currLen -= len(e)
                st.append(t[-1])
                currLen += len(t[-1])
                if t[-1].count(".") > 0:
                    isFile = True
            if isFile:
                print(st)
                maxLen = max(maxLen, currLen+len(st)-1)
        return maxLen
            
                