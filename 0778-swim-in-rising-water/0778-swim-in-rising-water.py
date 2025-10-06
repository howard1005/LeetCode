import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dy = [-1,0,1,0]
        dx = [0,1,0,-1]
        h = [(grid[0][0],0,0)]
        grid[0][0] = -1
        while h:
            t,y,x = heapq.heappop(h)
            print(t,y,x)
            if y==len(grid)-1 and x==len(grid[0])-1:
                return t
            for di in range(4):
                ny = y + dy[di]
                nx = x + dx[di]
                if ny<0 or nx<0 or ny>=len(grid) or nx>=len(grid[0]) or grid[ny][nx]==-1:
                    continue
                nt = grid[ny][nx]
                grid[ny][nx] = -1
                if nt <= t:
                    heapq.heappush(h,(t,ny,nx))
                else:
                    heapq.heappush(h,(nt,ny,nx))
        return -1