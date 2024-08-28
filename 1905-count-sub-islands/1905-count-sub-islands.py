class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        m,n = len(grid1),len(grid1[0])

        dy,dx = [-1,0,1,0],[0,1,0,-1]

        vis = set()
        def bfs(i,j):
            ret = True if grid1[i][j] else False
            
            dq = deque()

            vis.add((i,j))
            dq.append((i,j))

            while dq:
                y,x = dq.popleft()

                for di in range(4):
                    ny,nx = y+dy[di],x+dx[di]
                    if ny<0 or nx<0 or ny>=m or nx>=n or grid2[ny][nx] == 0 or (ny,nx) in vis:
                        continue
                    if grid1[ny][nx] == 0:
                        ret = False
                    vis.add((ny,nx))
                    dq.append((ny,nx))

            return ret

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] and (i,j) not in vis:
                    if bfs(i,j):
                        ans += 1

        return ans 


        