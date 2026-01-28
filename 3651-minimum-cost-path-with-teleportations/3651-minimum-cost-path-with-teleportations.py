class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        ans = inf

        # print('org')
        # for r in grid:
        #     print(r)
            
        m,n = len(grid),len(grid[0])
        
        l = []
        for i in range(m):
            for j in range(n):
                l.append((grid[i][j],i,j))
        l.sort()
        # print('l',l)

        dp = [[[inf for _ in range(k+1)] for _ in range(n)] for _ in range(m)]
        for kk in range(k+1):
            dp[-1][-1][kk] = 0

        d = defaultdict(lambda:inf)
        
        for kk in range(k+1):
            # print(kk,d)
            for c,i,j in l:
                if kk>0:
                    dp[i][j][kk] = min(dp[i][j][kk],d[c])
            for i in range(m-1,-1,-1):
                for j in range(n-1,-1,-1):
                    c = grid[i][j]
                    if i+1<m:
                        dp[i][j][kk] = min(dp[i][j][kk],dp[i+1][j][kk]+grid[i+1][j])
                    if j+1<n:
                        dp[i][j][kk] = min(dp[i][j][kk],dp[i][j+1][kk]+grid[i][j+1])
                    d[c] = min(d[c],dp[i][j][kk])
            mnc = inf
            for c,i,j in l:
                mnc = min(mnc,d[c])
                d[c] = mnc
            # print('f',dp)


        # for kk in range(k+1):
        #     print(f'\n{kk}th')
        #     for i in range(m):
        #         for j in range(n):
        #             print(dp[i][j][kk],' ',end='')
        #         print()

        ans = dp[0][0][k]
            
        return ans