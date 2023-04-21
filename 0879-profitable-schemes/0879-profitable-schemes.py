class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 1000000007
        
        dp = [[[0 for _ in range(minProfit+1)] for _ in range(n+1)] for _ in range(len(group))]
        
        for j in range(n+1):
            for k in range(minProfit+1):
                if group[-1] <= j and profit[-1] >= k:
                    dp[-1][j][k] = 1
                if k == 0:
                    dp[-1][j][k] += 1
                    
        for i in range(len(group)-2,-1,-1):
            for j in range(n+1):
                for k in range(minProfit+1):
                    if group[i] <= j:
                        jj = j - group[i]
                        kk = max(0,k - profit[i]) 
                        dp[i][j][k] = (dp[i][j][k] + dp[i+1][jj][kk]) % MOD
                    dp[i][j][k] = (dp[i][j][k] + dp[i+1][j][k]) % MOD         
                        
        return dp[0][n][minProfit]