class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dy,dx = [-2,-1,1,2,2,1,-1,-2],[1,2,2,1,-1,-2,-2,-1]
        
        dp = [[[0 for _ in range(k+1)] for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                dp[i][j][0] = 1
        
        for kk in range(1,k+1):
            for i in range(n):
                for j in range(n):
                    for di in range(8):
                        ni,nj = i+dy[di],j+dx[di]
                        if ni<0 or nj<0 or ni>=n or nj>=n:
                            continue
                        dp[i][j][kk] += (1/8)*dp[ni][nj][kk-1]
                        
        return dp[row][column][k]