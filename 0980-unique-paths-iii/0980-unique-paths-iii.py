class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        vis = [[0 for _ in range(n)] for _ in range(m)]
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        cnt = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sy,sx = i,j
                if grid[i][j] == 2:
                    ey,ex = i,j
                if grid[i][j] != -1:
                    cnt += 1
        #print(cnt)
        
        ans = 0
        def dfs(y,x,d):
            #print((y,x))
            nonlocal ans
            if (y,x) == (ey,ex):
                if d == cnt:
                    ans += 1
                    #print(ans)
                return
            for di in range(4):
                ny,nx = y+dy[di],x+dx[di]
                if ny<0 or nx<0 or ny>=m or nx>=n or vis[ny][nx] or grid[ny][nx] == -1:
                    continue
                vis[ny][nx] = 1
                dfs(ny,nx,d+1)
                vis[ny][nx] = 0
        vis[sy][sx] = 1
        dfs(sy,sx,1)
        vis[sy][sx] = 0
        
        return ans