class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 1000000007
        dp = [[0 for _ in range(fuel+1)] for _ in range(len(locations))]
        
        for j in range(fuel+1):
            dp[finish][j] = 1
            
        for j in range(1,fuel+1):
            for i in range(len(locations)):
                for k in range(len(locations)):
                    if i == k:
                        continue
                    cost = abs(locations[i]-locations[k])
                    if cost > j:
                        continue
                    dp[i][j] += dp[k][j-cost]
                    dp[i][j] %= MOD
        
        return dp[start][fuel]