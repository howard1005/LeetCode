class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [[-inf,inf] for _ in range(n)]
        dp[-1] = [stoneValue[-1],0]
        
        tot = sum(stoneValue)
        
        for i in range(n-2,-1,-1):
            for j in range(2):
                cum = 0
                for k in range(3):
                    if i+k >= n:
                        continue
                    if j == 0:
                        cum += stoneValue[i+k]
                        dp[i][j] = max(dp[i][j], (dp[i+k+1][j^1] if i+k+1 < n else 0) + cum)
                    else:
                        dp[i][j] = min(dp[i][j], (dp[i+k+1][j^1] if i+k+1 < n else 0))
                        
        if dp[0][0] > tot/2:
            return "Alice"
        elif dp[0][0] < tot/2:
            return "Bob"
        return "Tie"