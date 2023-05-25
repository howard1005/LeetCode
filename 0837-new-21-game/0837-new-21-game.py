class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0
        
        p = 1/maxPts
        dp = [[0.0,0.0] for _ in range(k)]
        base = min(maxPts,n-k+1)*p
        dp[-1] = [base,base]
        
        for i in range(len(dp)-2,-1,-1):
            if i+maxPts >= k:
                dp[i][0] += p * min(i+maxPts-k+1,n-k+1)
                dp[i][0] += p * dp[i+1][1]
            else:
                
                dp[i][0] += p * (dp[i+1][1] - (dp[i+maxPts+1][1] if i+maxPts < k-1 else 0 ))
            dp[i][1] = dp[i+1][1] + dp[i][0]
        
        return dp[0][0]