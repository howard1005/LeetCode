class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        
        m,n = len(grid),len(grid[0])

        ans = [[1 for _ in range(n)] for _ in range(m)]

        dpt = [[grid[i][j]%MOD for j in range(n)] for i in range(m)]
        dpl = [[grid[i][j]%MOD for j in range(n)] for i in range(m)]
        dpr = [[grid[i][j]%MOD for j in range(n)] for i in range(m)]
        dpb = [[grid[i][j]%MOD for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(1,n):
                dpl[i][j] *= dpl[i][j-1]
                dpl[i][j] %= MOD

        for i in range(m):
            for j in range(n-2,-1,-1):
                dpr[i][j] *= dpr[i][j+1]
                dpr[i][j] %= MOD

        for i in range(m):
            for j in range(n):
                if i-1 >= 0:
                    dpt[i][j] *= dpt[i-1][j]
                if j-1 >= 0:
                    dpt[i][j] *= dpl[i][j-1]
                dpt[i][j] %= MOD

        for i in range(m-1,-1,-1):
            for j in range(n):
                if i+1 < m:
                    dpb[i][j] *= dpb[i+1][j]
                if j-1 >= 0:
                    dpb[i][j] *= dpl[i][j-1]
                dpb[i][j] %= MOD

        
        for i in range(m):
            for j in range(n):
                if i-1 >= 0:
                    ans[i][j] *= dpt[i-1][n-1]
                if j-1 >= 0:
                    ans[i][j] *= dpl[i][j-1]
                if j+1 < n:
                    ans[i][j] *= dpr[i][j+1]
                if i+1 < m:
                    ans[i][j] *= dpb[i+1][n-1]
                ans[i][j] %= MOD
                

        return ans