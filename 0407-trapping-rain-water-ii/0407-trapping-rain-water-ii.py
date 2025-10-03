from heapq import heappush,heappop

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ans = 0

        dy,dx = [-1,0,1,0],[0,1,0,-1]

        m,n = len(heightMap),len(heightMap[0])

        vis = set()

        cnthq = []
        mxh = 0

        for i in range(m):
            for j in range(n):
                h = heightMap[i][j]
                heappush(cnthq,h)
                mxh = max(mxh,h)

        hq = []

        for i in range(m):
            h = heightMap[i][0]
            vis.add((i,0))
            heappush(hq,(h,i,0))
            if n > 1:
                h = heightMap[i][n-1]
                vis.add((i,n-1))
                heappush(hq,(h,i,n-1))

        for j in range(1,n-1):
            h = heightMap[0][j]
            vis.add((0,j))
            heappush(hq,(h,0,j))
            if m > 1:
                h = heightMap[m-1][j]
                vis.add((m-1,j))
                heappush(hq,(h,m-1,j))

        cnt = 0
        ucnt = 0
        
        for h in range(mxh+1):
            while cnthq and cnthq[0] <= h:
                heappop(cnthq)
                cnt += 1
            
            while hq and hq[0][0] <= h:
                th,y,x = heappop(hq)
                ucnt += 1
                for di in range(4):
                    ny,nx = y+dy[di],x+dx[di]
                    if ny<0 or nx<0 or ny>=m or nx>=n or (ny,nx) in vis:
                        continue
                    vis.add((ny,nx))
                    heappush(hq,(heightMap[ny][nx],ny,nx))

            ans += cnt-ucnt

        return ans
