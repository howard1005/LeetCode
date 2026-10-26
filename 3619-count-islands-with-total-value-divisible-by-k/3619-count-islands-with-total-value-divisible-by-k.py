class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        ans = 0

        m,n = len(grid),len(grid[0])

        dy,dx = [-1,0,1,0],[0,1,0,-1]

        vis = set()

        def bfs(y,x):
            ret = 0
            vis.add((y,x))
            dq = deque([(y,x)])
            tot = 0
            while dq:
                i,j = dq.popleft()
                tot += grid[i][j]
                # print(i,j,tot)
                for di in range(4):
                    ni,nj = i+dy[di],j+dx[di]
                    if ni<0 or nj<0 or ni>=m or nj>=n or grid[ni][nj]==0:
                        continue
                    if (ni,nj) in vis:
                        continue
                    vis.add((ni,nj))
                    dq.append((ni,nj))

            if tot%k == 0:
                ret = 1 

            return ret

        for y in range(m):
            for x in range(n):
                if (y,x) in vis or grid[y][x] == 0:
                    continue
                ans += bfs(y,x)

        return ans