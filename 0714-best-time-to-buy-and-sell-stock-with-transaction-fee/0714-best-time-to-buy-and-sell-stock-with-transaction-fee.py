class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[-1][1] = prices[-1]
        
        for i in range(len(prices)-2,-1,-1):
            dp[i][0] = max(dp[i+1][0],dp[i+1][1]-prices[i]-fee)
            dp[i][1] = max(dp[i+1][1],dp[i+1][0]+prices[i])
            
        return dp[0][0]