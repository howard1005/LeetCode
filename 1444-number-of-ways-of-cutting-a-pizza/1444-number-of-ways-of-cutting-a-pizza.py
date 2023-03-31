class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        
        MOD = 1000000007
        
        r,c = len(pizza),len(pizza[0])
        
        cm = [[1 if pizza[i][j] == 'A' else 0 for j in range(c)] for i in range(r)]
        
        for i in range(r-2,-1,-1):
            cm[i][-1] += cm[i+1][-1]
        for j in range(c-2,-1,-1):
            cm[-1][j] += cm[-1][j+1]
        for i in range(r-2,-1,-1):
            for j in range(c-2,-1,-1):
                cm[i][j] += cm[i+1][j] + cm[i][j+1] - cm[i+1][j+1]
        
        dp = [[[0 for _ in range(k)] for _ in range(c)] for _ in range(r)]
        
        
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                if cm[i][j] > 0:
                    dp[i][j][-1] = 1
                for kk in range(k-1):
                    for ii in range(i,r):
                        if cm[i][j] - cm[ii][j] > 0:
                            dp[i][j][kk] = (dp[i][j][kk] + dp[ii][j][kk+1])%MOD
                    for jj in range(j,c):
                        if cm[i][j] - cm[i][jj] > 0:
                            dp[i][j][kk] = (dp[i][j][kk] + dp[i][jj][kk+1])%MOD
        
        return dp[0][0][0]