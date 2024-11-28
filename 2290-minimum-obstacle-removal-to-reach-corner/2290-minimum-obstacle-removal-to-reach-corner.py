from heapq import heappush,heappop

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ans = inf
        
        dy,dx = [-1,0,1,0],[0,1,0,-1]

        m,n = len(grid),len(grid[0])

        h = [(0,0,0)]
        vis = set([(0,0)])

        while h:
            c,y,x = heappop(h)
            if y == m-1 and x == n-1:
                ans = c
                break
            for di in range(4):
                ny,nx = y+dy[di],x+dx[di]
                if ny<0 or nx<0 or ny>=m or nx>=n or (ny,nx) in vis:
                    continue
                vis.add((ny,nx))
                if grid[ny][nx]:
                    heappush(h,(c+1,ny,nx))
                else:
                    heappush(h,(c,ny,nx))

        return ans