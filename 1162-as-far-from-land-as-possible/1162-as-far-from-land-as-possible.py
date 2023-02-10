class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ans = 0
        
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        n = len(grid)
        def bfs(base):
            ret = 0
            vis = {}
            dq = deque()
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == base:
                        vis[(i,j)] = 1
                        dq.append((i,j,0))
            while dq:
                y,x,dist = dq.popleft()
                ret = dist
                for di in range(4):
                    ny,nx = y+dy[di],x+dx[di]
                    if ny<0 or nx<0 or ny>=n or nx>=n or (ny,nx) in vis or grid[ny][nx] == base:
                        continue
                    vis[(ny,nx)] = 1
                    dq.append((ny,nx,dist+1))
            return ret
        
        ans = bfs(1)
        
        return ans if ans else -1