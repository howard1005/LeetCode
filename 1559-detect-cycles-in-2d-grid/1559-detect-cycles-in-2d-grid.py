class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        m,n = len(grid),len(grid[0])

        def idx(i,j):
            # print(i,j,i*m+j)
            return i*n+j

        def ij(idx):
            return idx//n,idx%n

        el = []
        for i in range(m):
            for j in range(n):
                for di in [1,2]:
                    ni,nj = i+dy[di],j+dx[di]
                    if ni<0 or nj<0 or ni>=m or nj>=n:
                        continue
                    if grid[ni][nj] == grid[i][j]:
                        el.append((idx(i,j),idx(ni,nj)))
        # print(el)

        pars = [i for i in range(m*n)]

        def find(i):
            tl = []
            # print(i)
            while pars[i] != i:
                tl.append(i)
                i = pars[i]
            for j in tl:
                pars[j] = i
            return i

        def union(i,j):
            pi,pj = find(i),find(j)
            pars[pj] = pi

        for a,b in el:
            if find(a) == find(b):
                return True
            union(a,b)
                
        return False
