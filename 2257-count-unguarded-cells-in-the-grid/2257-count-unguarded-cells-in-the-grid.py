class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        dy,dx = [-1,0,1,0],[0,1,0,-1]

        bd = [[0 for _ in range(n)] for _ in range(m)]

        dq = deque()
        vis = set()

        for y,x in walls:
            bd[y][x] = -1

        for y,x in guards:
            for di in range(4):
                vis.add((y,x,di))
                dq.append((y,x,di))
            
        while dq:
            y,x,di = dq.popleft()
            bd[y][x] = 1

            ny,nx = y+dy[di],x+dx[di]
            if ny<0 or nx<0 or ny>=m or nx>=n or (ny,nx,di) in vis or bd[ny][nx] == -1:
                continue

            vis.add((ny,nx,di))
            dq.append((ny,nx,di))

        ans = 0

        for i in range(m):
            for j in range(n):
                if bd[i][j] == 0:
                    ans += 1

        return ans


                
            
            

                
                

            
            