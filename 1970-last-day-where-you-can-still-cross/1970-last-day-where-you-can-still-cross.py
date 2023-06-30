class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        
        b = [[0 for _ in range(col)] for _ in range(row)]
        
        def valid(t):
            for i in range(t):
                y,x = cells[i]
                b[y-1][x-1] = 1
            ret = False
            vis = {}
            dq = deque()
            for j in range(col):
                if b[0][j] == 0:
                    dq.append((0,j))
            while dq:
                y,x = dq.popleft()
                if y == row-1:
                    ret = True
                    break
                for di in range(4):
                    ny,nx = dy[di]+y,dx[di]+x
                    if ny<0 or nx<0 or ny>=row or nx>=col or b[ny][nx] or (ny,nx) in vis:
                        continue
                    vis[(ny,nx)] = 1
                    dq.append((ny,nx))
            for i in range(t):
                y,x = cells[i]
                b[y-1][x-1] = 0
            return ret
        
        ans = -1
        lo,hi = 0,row*col
        while lo <= hi:
            mi = (lo+hi)//2
            if valid(mi):
                ans = mi
                lo = mi+1
            else:
                hi = mi-1
        
        return ans