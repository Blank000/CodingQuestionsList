class Solution:
    def longestPrefix(self, s: str) -> str:
        # This is KMP algorithm
        lps = [0]*len(s)
        idx = 0
        i = 1
        while i < len(s):
            if s[i] == s[idx]:
                lps[i] = idx + 1
                i += 1
                idx += 1
            else:
                if idx > 0 and s[i] != s[idx]:
                    idx = lps[idx-1]
                else:
                    i += 1
        if lps[-1] == -1:
            return ""
        return s[:lps[-1]]