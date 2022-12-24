class Solution:
    def numTilings(self, n: int) -> int:
        mod = 1000000007
        dp = [[-1,-1,-1,-1] for _ in range(n)]
        def dfs(i,sta):
            if i == n:
                if sta == 0:
                    return 1
                else:
                    return 0
            if dp[i][sta] != -1:
                return dp[i][sta]
            dp[i][sta] = 0
            ret = 0 
            if sta == 0:
                ret += dfs(i+1,0)
                ret += dfs(i+1,1)
                ret += dfs(i+1,2)
                ret += dfs(i+1,3)
            elif sta == 1:
                ret += dfs(i+1,2)
                ret += dfs(i+1,3)
            elif sta == 2:
                ret += dfs(i+1,1)
                ret += dfs(i+1,3)
            else:
                ret += dfs(i+1,0)
            dp[i][sta] = ret % mod
            return ret
        return dfs(0,0) % mod