class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for _ in range(len(prices))]
        for i in range(len(prices)-2,-1,-1):
            buy_price = prices[i]
            dp[i] = dp[i+1]
            for j in range(i+1,len(prices)):
                sell_price = prices[j]
                profit = sell_price-buy_price
                if j+2 < len(prices):
                    profit += dp[j+2]
                dp[i] = max(dp[i],profit)
        return dp[0]