import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        r,c = len(heights),len(heights[0])
        print(r,c)
        vis = [[float('inf') for _ in range(c)] for _ in range(r)]
        h = []
        vis[0][0] = 0
        heapq.heappush(h,(0,0,0))
        while h:
            d,y,x = heapq.heappop(h)
            if y == r-1 and x == c-1:
                return d
            for di in range(4):
                ny=y+dy[di]
                nx=x+dx[di]
                if ny<0 or nx<0 or ny>=r or nx>=c:
                    continue
                nd = max(d,abs(heights[y][x]-heights[ny][nx]))
                if vis[ny][nx] <= nd:
                    continue
                vis[ny][nx] = nd
                heapq.heappush(h,(nd,ny,nx))
                
        return -1