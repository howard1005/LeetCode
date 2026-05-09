class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m,n = len(grid),len(grid[0])
        
        dy,dx = [-1,0,1,0],[0,1,0,-1]

        ans = [[0 for _ in range(n)] for _ in range(m)]

        def proc(ofs,setl,mode):
            di = 3
            sy,sx = ofs,ofs
            y,x = sy,sx
            i = 0
            retl = []
            while 1:
                if mode == 0:
                    retl.append(grid[y][x])
                else:
                    ans[y][x] = setl[i]
                    i += 1
                ny,nx = y+dy[di],x+dx[di]
                if ny<ofs or nx<ofs or ny>=m-ofs or nx>=n-ofs:
                    di = (di+3)%4
                    ny,nx = y+dy[di],x+dx[di]
                if (ny,nx) == (sy,sx):
                    break
                y,x = ny,nx
            return retl

        for ofs in range(min(m,n)//2):
            l = proc(ofs,[],0)
            sl = [0 for _ in range(len(l))]
            for i in range(len(l)):
                sl[(i+k)%len(l)] = l[i]
            proc(ofs,sl,1)

        return ans