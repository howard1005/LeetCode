class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        dp = [[float('inf') for _ in range(d+1)] for _ in range(len(jobDifficulty)+1)]
        dp[-1][0] = 0
        
        for i in range(len(jobDifficulty)-1,-1,-1):
            for j in range(1,d+1):
                mx = 0
                for k in range(i, len(jobDifficulty)):
                    mx = max(mx,jobDifficulty[k])
                    dp[i][j] = min(dp[i][j], dp[k+1][j-1]+mx)
        
        
        return -1 if dp[0][d] == float('inf') else dp[0][d]
        