class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        
        def dfs(i,a):
            if i >= len(coins):
                return 1 if a == 0 else 0
            
            if dp[i][a] != -1:
                return dp[i][a]
            dp[i][a] = 0
            
            c = coins[i]
            cnt = 0
            while a-cnt*c >= 0:
                dp[i][a] += dfs(i+1,a-cnt*c)
                cnt += 1
        
            return dp[i][a]
                    
        return dfs(0,amount)