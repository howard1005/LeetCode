class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [inf for _ in range(n+1)]
        dp[0] = 0
        for i in range(n+1):
            if i+1 < n+1:
                dp[i+1] = min(dp[i+1],dp[i]+costs[i]+1**2)
            if i+2 < n+1:
                dp[i+2] = min(dp[i+2],dp[i]+costs[i+1]+2**2) 
            if i+3 < n+1:
                dp[i+3] = min(dp[i+3],dp[i]+costs[i+2]+3**2)
        # print(dp)
        return dp[-1]
                