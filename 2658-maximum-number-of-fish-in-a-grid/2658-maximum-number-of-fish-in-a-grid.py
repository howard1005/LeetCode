class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans = 0

        dy,dx = [-1,0,1,0],[0,1,0,-1]

        m,n = len(grid),len(grid[0])
        
        vis = set()
        def bfs(y,x):
            ret = 0
            
            vis.add((y,x))
            dq = deque([(y,x)])

            while dq:
                y,x = dq.popleft()
                ret += grid[y][x]
                for di in range(4):
                    ny,nx = y+dy[di],x+dx[di]
                    if ny<0 or nx<0 or ny>=m or nx>=n or (ny,nx) in vis:
                        continue
                    if grid[ny][nx] == 0:
                        continue
                    vis.add((ny,nx))
                    dq.append((ny,nx))
            
            return ret
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and (i,j) not in vis:
                    ans = max(ans,bfs(i,j))

        return ans