class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        ans = -1
        
        m,n = len(grid),len(grid[0])

        cd = {
            0:0,
            1:1,
            2:1
        }

        dp = [[defaultdict(lambda:-1) for _ in range(n)] for _ in range(m)]
        dp[0][0][cd[grid[0][0]]] = grid[0][0]

        for i in range(m):
            for j in range(n):
                d = dp[i][j]
                c,v = cd[grid[i][j]],grid[i][j]
                if i-1>=0:
                    ud = dp[i-1][j]
                    for uc,uv in ud.items():
                        if c+uc <= k:
                            d[c+uc] = max(d[c+uc],v+uv)
                if j-1>=0:
                    ud = dp[i][j-1]
                    for uc,uv in ud.items():
                        if c+uc <= k:
                            d[c+uc] = max(d[c+uc],v+uv)

        d = dp[-1][-1]
        # print(d)
        for kk in range(k+1):
            ans = max(ans,d[kk])

        return ans