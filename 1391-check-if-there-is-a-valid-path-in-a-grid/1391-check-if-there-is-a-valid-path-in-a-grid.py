class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        dy,dx = [-1,0,1,0],[0,1,0,-1]
        d = {
            1:{1,3},
            2:{0,2},
            3:{2,3},
            4:{1,2},
            5:{0,3},
            6:{0,1},
        }

        m,n = len(grid),len(grid[0])

        vis = set()
        vis.add((0,0))
        dq = deque([(0,0)])
        while dq:
            y,x = dq.popleft()
            if (y,x) == (m-1,n-1):
                return True
            esd = d[grid[y][x]]
            for di in esd:
                ny,nx = y+dy[di],x+dx[di]
                if ny<0 or nx<0 or ny>=m or nx>=n or (ny,nx) in vis:
                    continue
                nesd = d[grid[ny][nx]]
                ndi = (di+2)%4
                if ndi not in nesd:
                    continue
                vis.add((ny,nx))
                dq.append((ny,nx))

        return False