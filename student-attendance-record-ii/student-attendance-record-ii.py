class Solution:
    def checkRecord(self, n: int) -> int:
        '''
        On any day, either you can be late or you can be present (absent cases we will see later).
        So if present then consider cases dp[n-1], if L then there can be two scenarios, either you will be
        present at the previous day P or you can still be late L. If P in the last day, then dp[n-2], but it 
        you are L the last day then you cannot be L on previous to that day, becoz then the rule breaks. 
        So you will only consider the case PLL
        '''
        if n == 1:
            return 3
        dp = [0]*(n+1)
        MOD = 10**9 + 7
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        i = 3
        while i <= n:
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD
            i += 1
        res = dp[n]
        idx = 1
        while idx <= n:
            res += (dp[idx-1]*dp[n-idx])%MOD
            idx += 1
        return res%MOD