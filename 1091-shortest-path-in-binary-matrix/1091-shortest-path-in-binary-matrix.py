import heapq

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        dy,dx = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]
        r,c = len(grid),len(grid[0])
        vis = [[float('inf') for _ in range(c)] for _ in range(r)]
        h = []
        vis[0][0] = 1
        heapq.heappush(h,(1,0,0))
        while h:
            d,y,x = heapq.heappop(h)
            for di in range(8):
                ny,nx = y+dy[di],x+dx[di]
                if ny<0 or nx<0 or ny>=r or nx>=c or grid[ny][nx] or vis[ny][nx]<=d+1:
                    continue
                vis[ny][nx] = d+1
                heapq.heappush(h,(d+1,ny,nx))
        if vis[-1][-1] == float('inf'):
            return -1
        return vis[-1][-1]