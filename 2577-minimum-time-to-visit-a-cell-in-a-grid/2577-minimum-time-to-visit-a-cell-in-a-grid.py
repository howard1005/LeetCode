from heapq import heappush,heappop

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:

        if 1<min(grid[0][1],grid[1][0]):
            return -1
        
        dy,dx = [-1,0,1,0],[0,1,0,-1]

        m,n = len(grid),len(grid[0])

        vis = defaultdict(lambda:inf)
        vis[(0,0)] = 0
        h = [(0,0,0)]

        def normal(a,b):
            if a > b:
                if (a-b)%2:
                    return a+1
                else:
                    return a
            return b

        while h:
            t,y,x = heappop(h)
            if vis[(y,x)] != t:
                continue
            if (y,x) == (m-1,n-1):
                return t
            for di in range(4):
                ny,nx = y+dy[di],x+dx[di]
                
                if ny<0 or nx<0 or ny>=m or nx>=n:
                    continue
                nt = normal(grid[ny][nx],t+1)
                if vis[(ny,nx)]<=nt:
                    continue
                vis[(ny,nx)] = nt
                heappush(h,(nt,ny,nx))
        
        return -1