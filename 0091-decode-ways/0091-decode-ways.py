class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1 for _ in range(len(s))]    
        def dfs(idx):
            if idx == len(s):
                return 1
            if s[idx] == '0':
                return 0
            if dp[idx] != -1:
                return dp[idx]
            dp[idx] = 0
            if idx + 1 < len(s) and int(s[idx:idx+2]) <= 26:
                dp[idx] += dfs(idx+2)
            dp[idx] += dfs(idx+1)
            return dp[idx]
        return dfs(0)
            