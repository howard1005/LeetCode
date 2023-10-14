class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp = [[-1 for _ in range(len(cost)*2+1)] for _ in range(len(cost))]
        
        def dfs(i,fw):
            if fw == -len(cost):
                return 0
            if i >= len(cost):
                return 0 if fw <= 0 else inf
            
            j = fw + len(cost)
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = inf
            
            dp[i][j] = min(dp[i][j],dfs(i+1,fw+1))
            dp[i][j] = min(dp[i][j],dfs(i+1,max(-len(cost),fw-time[i]))+cost[i])
            
            return dp[i][j]
        
        ans = dfs(0,0)
        
        return ans