class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        dp[0]=1
        duplicate = collections.defaultdict(int)
        
        for i in range(1,len(s)+1):
            dp[i] += 2*dp[i-1]
            dp[i] -= dp[duplicate[s[i-1]]] if (s[i-1] in duplicate) else 0
            duplicate[s[i-1]] = i-1
            #print(duplicate, s[i-1], dp)
            
        return (dp[-1] - 1)%(10**9+7)