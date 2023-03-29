class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        d = set(days)
        dp = [0 for _ in range(400)]
        for i in range(365,-1,-1):
            if i in d:
                dp[i] = min(costs[0]+dp[i+1], costs[1]+dp[i+7], costs[2]+dp[i+30])
            else:
                dp[i] = dp[i+1]
        
        return dp[0]