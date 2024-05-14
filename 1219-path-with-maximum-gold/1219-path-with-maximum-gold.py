class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans = 0

        dy,dx = [-1,0,1,0],[0,1,0,-1]

        m,n = len(grid),len(grid[0])

        vis = set()
        dp = set()

        def dfs(y,x,c):
            nonlocal ans
            ans = max(ans,c)
            print(y,x,c)

            if (y,x,c) in dp:
                return
            dp.add((y,x,c))

            for di in range(4):
                ny,nx = y+dy[di],x+dx[di]
                if ny<0 or nx<0 or ny>=m or nx>=n or grid[ny][nx] == 0:
                    continue
                if (ny,nx) not in vis:
                    vis.add((ny,nx))
                    dfs(ny,nx,c+grid[ny][nx])
                    vis.remove((ny,nx))

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dp = set()
                    vis.add((i,j))
                    dfs(i,j,grid[i][j])
                    vis.remove((i,j))

        return ans