from heapq import heappush,heappop

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        dy,dx = [-1,0,1,0],[0,1,0,-1]

        m,n = len(moveTime),len(moveTime[0])

        vis = defaultdict(lambda:inf)
        hq = []
        vis[(0,0)] = 0
        heappush(hq,(0,0,0))

        while hq:
            c,y,x = heappop(hq)
            if c > vis[(y,x)]:
                continue
            if y == m-1 and x == n-1:
                return c
            for di in range(4):
                ny,nx = y+dy[di],x+dx[di]
                nc = c+moveTime[y][x]+1
                if ny<0 or nx<0 or ny>=m or nx>=n:
                    continue
                nc = c+1 if moveTime[ny][nx] <= c else moveTime[ny][nx]+1
                if vis[(ny,nx)] <= nc:
                    continue
                vis[(ny,nx)] = nc
                heappush(hq,(nc,ny,nx))
        