class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        MOD = 1000000007
        
        dp = [0 for _ in range(2*high)]
        
        for i in range(high-1,-1,-1):
            zi = i+zero 
            if low <= zi and zi <= high:
                dp[i] += 1
            oi = i+one 
            if low <= oi and oi <= high:
                dp[i] += 1
            dp[i] += dp[zi]
            dp[i] += dp[oi]
            dp[i] %= MOD
        
        return dp[0]