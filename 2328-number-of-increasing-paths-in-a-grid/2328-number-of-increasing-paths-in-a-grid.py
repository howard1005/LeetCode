class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        m,n = len(grid),len(grid[0])
        MOD = 1000000007
        
        ans = 0
        
        dp = [[1 for _ in range(n)] for _ in range(m)]
        
        for v,y,x in sorted([(-grid[i][j],i,j) for i in range(m) for j in range(n)]):
            for di in range(4):
                ny,nx = y+dy[di],x+dx[di]
                if ny<0 or nx<0 or ny>=m or nx>=n:
                    continue
                if grid[ny][nx] > -v:
                    dp[y][x] += dp[ny][nx]
            ans = (ans+dp[y][x])%MOD
                
        
        return ans