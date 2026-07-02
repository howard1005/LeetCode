from heapq import heappush,heappop

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        dy,dx = [-1,0,1,0],[0,1,0,-1]

        m,n = len(grid),len(grid[0])

        vis = defaultdict(lambda:inf)
        hq = []
        vis[(0,0)] = grid[0][0]
        heappush(hq,(grid[0][0],0,0))
        while hq:
            c,y,x = heappop(hq)
            if vis[(y,x)] != c:
                continue
            # print(c,y,x)
            if (y,x) == (m-1,n-1):
                return True
            for di in range(4):
                ny,nx = y+dy[di],x+dx[di]
                if ny<0 or nx<0 or ny>=m or nx>=n:
                    continue
                nc = c+grid[ny][nx]
                if vis[(ny,nx)] <= nc:
                    continue
                if nc >= health:
                    continue
                vis[(ny,nx)] = nc
                heappush(hq,(nc,ny,nx))

        return False