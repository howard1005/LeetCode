class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        ans = 0
        
        dy,dx = [-1,-1,1,1],[-1,1,1,-1]

        m,n = len(grid),len(grid[0])
        
        @cache
        def dfs(y,x,di,cdi):
            ret = 1

            nv = ((grid[y][x] if grid[y][x] != 1 else 0)^2)

            ny,nx = y+dy[di],x+dx[di]
            # print(y,x,di,cdi, "ny,nx,nv", ny,nx,nv )
            if ny>=0 and nx>=0 and ny<m and nx<n and grid[ny][nx] == nv:
                ret = max(ret,dfs(ny,nx,di,cdi)+1)

            ndi = (di+1)%4
            ny,nx = y+dy[ndi],x+dx[ndi]
            if cdi == 0 and ny>=0 and nx>=0 and ny<m and nx<n and grid[ny][nx] == (grid[y][x]^2):
                ret = max(ret,dfs(ny,nx,ndi,1)+1)

            return ret
            
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for di in range(4):
                        ans = max(ans,dfs(i,j,di,0))

        return ans