class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j and i < len(s) and j >= 0:
            while i < len(s) and j >= 0 and not s[i].isalnum():
                i += 1
            while i < len(s) and j >= 0 and not s[j].isalnum():
                j -= 1
            if i < j and i < len(s) and j >= 0 and s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            elif i < j and i < len(s) and j >= 0 and s[i].lower() != s[j].lower():
                return False
        return True
    