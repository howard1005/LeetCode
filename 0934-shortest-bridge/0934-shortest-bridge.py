class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        n = len(grid)        
        vis = {}
        
        def bfs1(sy,sx):
            ret = set()
            dq = deque()
            vis[(sy,sx)] = 1
            dq.append((sy,sx))
            while dq:
                y,x = dq.popleft()
                for di in range(4):
                    ny,nx = y+dy[di],x+dx[di]
                    if ny<0 or nx<0 or ny>=n or nx>=n or (ny,nx) in vis:
                        continue
                    if grid[ny][nx] == 0:
                        ret.add((y,x,0))
                        continue
                    vis[(ny,nx)] = 1
                    dq.append((ny,nx))
            return ret
        
        def bfs2(sl):
            dq = deque(sl)
            while dq:
                y,x,dist = dq.popleft()
                for di in range(4):
                    ny,nx = y+dy[di],x+dx[di]
                    if ny<0 or nx<0 or ny>=n or nx>=n or (ny,nx) in vis:
                        continue
                    if grid[ny][nx] == 1:
                        return dist
                    vis[(ny,nx)] = 1
                    dq.append((ny,nx,dist+1))
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    sl = bfs1(i,j)
                    return bfs2(sl)
                
        return -1