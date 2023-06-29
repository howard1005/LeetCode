class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        
        m,n = len(grid),len(grid[0])
        
        vis = defaultdict(lambda:inf)
        dq = deque([])
        
        ks = 0
        kd = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    vis[(i,j,0)] = 0
                    dq.append((0,i,j,0))
                elif  grid[i][j] in ['#','.']:
                    pass
                else:
                    c = grid[i][j]
                    if c.islower():
                        kd[c] = ks
                        ks += 1
        
        while dq:
            dist,y,x,mask = dq.popleft()
            # print(dist,y,x,mask)
            if mask == (1<<ks)-1:
                return dist
            for di in range(4):
                ny,nx = dy[di]+y,dx[di]+x
                if ny<0 or nx<0 or ny>=m or nx>=n:
                    continue
                c = grid[ny][nx]
                if c == '#':
                    continue
                if c.isupper() and (mask&(1<<kd[c.lower()])) == 0:
                    continue
                nmask = mask
                if c in kd:
                    i = kd[c]
                    nmask |= (1<<i)
                if (ny,nx,nmask) in vis:
                    continue
                vis[(ny,nx,nmask)] = dist+1
                dq.append((dist+1,ny,nx,nmask))
        
                
        return -1
        