class Solution:
    def minInsertions(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(s)-1):
            j = i + 1
            if s[i] != s[j]:
                dp[i][j] = 1
            
        for ofs in range(2,len(s)):
            for i in range(len(s)-ofs):
                j = i + ofs
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j],dp[i][j-1]) + 1          
            
        return dp[0][-1]