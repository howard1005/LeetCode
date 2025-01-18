from heapq import heappush,heappop

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        dy,dx = [0,0,0,1,-1],[0,1,-1,0,0]

        m,n = len(grid),len(grid[0])

        vis = defaultdict(lambda:inf)

        hq = [(0,0,0)]

        while hq:
            c,y,x = heappop(hq)
            if y==m-1 and x==n-1:
                return c
            if vis[(y,x)] < c:
                continue
            for di in range(1,5):
                ny,nx = y+dy[di],x+dx[di]
                if ny<0 or nx<0 or ny>=m or nx>=n:
                    continue
                nc = c + (1 if grid[y][x]!=di else 0)
                if vis[(ny,nx)] <= nc:
                    continue
                vis[(ny,nx)] = nc
                heappush(hq,(nc,ny,nx))

        return -1