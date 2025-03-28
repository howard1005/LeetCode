from heapq import heappush,heappop

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ans = [0 for _ in range(len(queries))]

        m,n = len(grid),len(grid[0])

        dy,dx = [-1,0,1,0],[0,1,0,-1]

        l = [(q,i) for i,q in enumerate(queries)]
        l.sort()

        cnt = 0
        vis = set([(0,0)])
        hq = [(grid[0][0],0,0)]
        for q,i in l:
            while hq and hq[0][0] < q:
                _,y,x = heappop(hq)
                cnt += 1
                for di in range(4):
                    ny,nx = y+dy[di],x+dx[di]
                    if ny<0 or nx<0 or ny>=m or nx>=n or (ny,nx) in vis:
                        continue
                    vis.add((ny,nx))
                    heappush(hq,(grid[ny][nx],ny,nx))
            ans[i] = cnt

        return ans