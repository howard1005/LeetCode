class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = [[-1 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        def dfs(a, b, c):
            if a == len(s1) and b == len(s2) and c == len(s3):
                return 1
            elif c == len(s3):
                return 0
            if dp[a][b] != -1:
                return dp[a][b]
            dp[a][b] = 0
            if a < len(s1) and s1[a] == s3[c]:
                dp[a][b] = dfs(a+1,b,c+1)
            if dp[a][b] == False and b < len(s2) and s2[b] == s3[c]:
                dp[a][b] = dfs(a,b+1,c+1)            
            return dp[a][b]
        return dfs(0,0,0)