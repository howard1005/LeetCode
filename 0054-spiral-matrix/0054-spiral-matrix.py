class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dy = [-1,0,1,0]
        dx = [0,1,0,-1]
        ans = []
        m,n = len(matrix),len(matrix[0])
        
        y,x = 0,0
        di = 1 if n == 1 else 0
        ans.append(matrix[y][x])
        matrix[y][x] = 101
        while 1:
            di = (di+1)%4
            cnt = 0
            while 1:
                ny,nx = y+dy[di],x+dx[di]
                if ny < 0 or nx < 0 or ny >= m or nx >= n or matrix[ny][nx] == 101:
                    break
                ans.append(matrix[ny][nx])
                matrix[ny][nx] = 101
                y,x = ny,nx
                cnt += 1
            
            if cnt == 0:
                break
                
        return ans 