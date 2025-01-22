class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        dy,dx = [-1,0,1,0],[0,1,0,-1]

        m,n = len(isWater),len(isWater[0])

        ans = [[0 for _ in range(n)] for _ in range(m)]

        vis = set()
        dq = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    vis.add((i,j))
                    dq.append((i,j,0))

        while dq:
            y,x,h = dq.popleft()
            for di in range(4):
                ny,nx = y+dy[di],x+dx[di]
                if ny<0 or nx<0 or ny>=m or nx>=n or (ny,nx) in vis:
                    continue
                vis.add((ny,nx))
                dq.append((ny,nx,h+1))
                ans[ny][nx] = h+1

        return ans
            