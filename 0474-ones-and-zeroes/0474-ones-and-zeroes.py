class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs.sort(key=lambda x: -len(x))
        
        dp = [[[-1 for _ in range(n+1)] for _ in range(m+1)] for _ in range(len(strs))]
        
        l = [[0 for _ in range(2)] for _ in range(len(strs))]
        for i,s in enumerate(strs):
            for c in s:
                if c == '0':
                    l[i][0] += 1
                else:
                    l[i][1] += 1            
        
        z,o = l[-1]
        for j in range(m+1):
            for k in range(n+1):
                if j-z>=0 and k-o>=0:
                    dp[-1][j][k] = 1
                else:
                    dp[-1][j][k] = 0
                    
                    
        def dfs(i,j,k):
            if dp[i][j][k] != -1:
                return dp[i][j][k]
            
            z,o = l[i]
            dp[i][j][k] = max(dp[i][j][k],dfs(i+1,j,k))
            if j-z>=0 and k-o>=0:
                dp[i][j][k] = max(dp[i][j][k],dfs(i+1,j-z,k-o)+1)
                
            return dp[i][j][k]
        
        return dfs(0,m,n)
    
#         for i in range(len(strs)-2,-1,-1):
#             z,o = l[i]
#             for j in range(m+1):
#                 for k in range(n+1):
#                     dp[i][j][k] = max(dp[i][j][k],dp[i+1][j][k])
#                     if j-z>=0 and k-o>=0:
#                         dp[i][j][k] = max(dp[i][j][k],dp[i+1][j-z][k-o]+1)
                    
#         return dp[0][m][n]