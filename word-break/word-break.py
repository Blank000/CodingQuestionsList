class Solution:
    def wordBreak(self, s: str, dic: List[str]) -> bool:
        # We can solve this using the kind of level order traversal that I have defined for myself
        #dp = [False]*(len(s)+1)
        #dp[0] = True
        idx = [-1]
        for i in range(len(s)):
            for j in idx:
                if s[j+1:i+1] in dic:
                    idx.append(i)
                    #dp[i+1] = True
                    if i == len(s)-1:
                        return True
                    break
        return False