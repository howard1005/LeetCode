class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 1000000007
        
        dp = [0 for i in range(len(s) + 1)]
        dp[-1] = 1
        
        for i in range(len(s)-1,-1,-1):
            if s[i] == '0':
                continue
            
            n = 0
            for j in range(i,len(s)):
                n = n * 10 + int(s[j])
                if n <= k:
                    dp[i] = (dp[i] + dp[j+1]) % MOD
                else:
                    break
                    
        return dp[0]
            