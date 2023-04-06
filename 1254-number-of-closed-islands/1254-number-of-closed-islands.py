class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        
        r,c = len(grid),len(grid[0])
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        
        def bfs(sy,sx):
            ret = 1
            grid[sy][sx] = -1
            dq = deque([(sy,sx)])
            while dq:
                y,x = dq.popleft()
                for di in range(4):
                    ny,nx = y+dy[di],x+dx[di]
                    if ny<0 or nx<0 or ny>=r or nx>=c:
                        ret = 0
                        continue
                    if grid[ny][nx] != 0:
                        continue
                    grid[ny][nx] = -1
                    dq.append((ny,nx))
                    
            return ret
        
        for y in range(r):
            for x in range(c):
                if grid[y][x] == 0:
                    ans += bfs(y,x)
            
        return ans