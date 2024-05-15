from heapq import heappush,heappop

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        ans = 0

        dy,dx = [-1,0,1,0],[0,1,0,-1]
        
        n = len(grid)

        mp = [[inf for _ in range(n)] for _ in range(n)]

        dq = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    mp[i][j] = 0
                    dq.append((i,j,0))
        
        while dq:
            y,x,sf = dq.popleft()
            for di in range(4):
                ny,nx = y+dy[di],x+dx[di]
                if ny<0 or nx<0 or ny>=n or nx>=n or mp[ny][nx]<=sf+1:
                    continue
                mp[ny][nx] = sf+1
                dq.append((ny,nx,sf+1))

        vis = defaultdict(int)

        hq = [(-mp[0][0],0,0)]
        while hq:
            sf,y,x = heappop(hq)
            sf = -sf
            if (y,x) == (n-1,n-1):
                ans = sf
                break
            for di in range(4):
                ny,nx = y+dy[di],x+dx[di]
                if ny<0 or nx<0 or ny>=n or nx>=n:
                    continue
                nsf = min(sf,mp[ny][nx])
                if vis[(ny,nx)]>=nsf:
                    continue
                vis[(ny,nx)] = nsf
                heappush(hq,(-nsf,ny,nx))

        return ans
            
