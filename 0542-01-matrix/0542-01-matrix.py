class Solution:
    def updateMatrix(self, matrix):
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        r,c = len(matrix),len(matrix[0])
        ans = [[0 for _ in range(c)] for _ in range(r)]
        
        vis = {}
        dq = deque()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    vis[(i,j)] = 1
                    dq.append((i,j,0))
                    
        while dq:
            y,x,dist = dq.popleft()
            for di in range(4):
                ny,nx = y+dy[di],x+dx[di]
                if ny<0 or nx<0 or ny>=r or nx>=c or (ny,nx) in vis:
                    continue
                vis[(ny,nx)] = 1
                ans[ny][nx] = dist+1
                dq.append((ny,nx,dist+1))
            
        return ans