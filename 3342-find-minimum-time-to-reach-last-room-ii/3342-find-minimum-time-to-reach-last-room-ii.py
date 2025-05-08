from heapq import heappush,heappop

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        ans = 0

        n,m = len(moveTime),len(moveTime[0])

        dy,dx = [-1,0,1,0],[0,1,0,-1]

        vis = defaultdict(lambda:inf)
        hq = []
        vis[(0,0)] = 0
        heappush(hq,(0,0,0,0))

        while hq:
            c,y,x,step = heappop(hq)
            if vis[(y,x)] != c:
                continue
            if y == n-1 and x == m-1:
                ans = c
                break
            for di in range(4):
                ny,nx = y+dy[di],x+dx[di]
                if ny<0 or nx<0 or ny>=n or nx>=m:
                    continue
                nc = (moveTime[ny][nx] if moveTime[ny][nx]>=c else c) + step+1
                if vis[(ny,nx)] <= nc:
                    continue
                vis[(ny,nx)] = nc
                heappush(hq,(nc,ny,nx,step^1))

        return ans