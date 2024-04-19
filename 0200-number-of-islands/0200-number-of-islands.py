from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        def bfs(sy,sx):
            grid[sy][sx] = 0
            dq = deque([(sy,sx)])
            while dq:
                y,x = dq.popleft()
                for di in range(4):
                    ny,nx = y+dy[di],x+dx[di]
                    if ny<0 or nx<0 or ny>=m or nx>=n or grid[ny][nx]=='0':
                        continue
                    grid[ny][nx] = '0'
                    dq.append((ny,nx))
                    
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i,j)
                    ans += 1
        return ans