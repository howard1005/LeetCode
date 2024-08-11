class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        
        dy,dx = [-1,0,1,0],[0,1,0,-1]

        def bfs(y,x,vis):
            vis.add((y,x))
            dq = deque([(y,x)])
            while dq:
                i,j = dq.popleft()
                for di in range(4):
                    ni,nj = i+dy[di],j+dx[di]
                    if ni<0 or nj<0 or ni>=len(grid) or nj>=len(grid[0]) or (ni,nj) in vis or grid[ni][nj]==0:
                        continue
                    vis.add((ni,nj))
                    dq.append((ni,nj))
                
        
        def valid():
            cnt = 0
            vis = set()
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] and (i,j) not in vis:
                        cnt += 1
                        bfs(i,j,vis)
            return cnt > 1 or cnt == 0

        if valid():
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    grid[i][j] = 0
                    if valid():
                        return 1
                    grid[i][j] = 1

        return 2