class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1.0
        
        # 1. 4 0
        # 2. 3 1
        # 3. 2 2
        # 4. 1 3
        
        k = n//25+(1 if n%25 else 0)+1
        dp = [[0.0 for _ in range(k)] for _ in range(k)]
        
        dp[0][0] = 0.5
        for j in range(1,k):
            dp[0][j] = 1.0
            
        for i in range(1,k):
            for j in range(1,k):
                dp[i][j] += 0.25*dp[max(0,i-4)][max(0,j)]
                dp[i][j] += 0.25*dp[max(0,i-3)][max(0,j-1)]
                dp[i][j] += 0.25*dp[max(0,i-2)][max(0,j-2)]
                dp[i][j] += 0.25*dp[max(0,i-1)][max(0,j-3)]
        
        return dp[-1][-1]