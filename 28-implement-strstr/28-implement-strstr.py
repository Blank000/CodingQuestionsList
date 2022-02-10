class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Implementing KMP algorithm here
        # First we need to create lps array
        def createLpsArray(s):
            lps = [0]*len(s)
            idx = 0
            i = 1
            while i < len(s):
                while s[i] != s[idx] and idx > 0:
                    idx = lps[idx-1]
                if s[i] == s[idx]:
                    idx += 1
                lps[i] = idx
                i += 1
            return lps
        lps = createLpsArray(needle)
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            while haystack[i] != needle[j] and j > 0:
                j = lps[j-1]
            if haystack[i] == needle[j]:
                j += 1
            i += 1
        if j == len(needle):
            return i-j
        return -1