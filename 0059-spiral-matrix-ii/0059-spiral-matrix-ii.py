class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        y,x = 0,0
        di = 1
        i = 1
        while i<=n*n:
            ans[y][x] = i
            ny,nx = y+dy[di],x+dx[di]
            if ny<0 or nx<0 or ny>=n or nx>=n or ans[ny][nx]:
                di = (di+1)%4
                ny,nx = y+dy[di],x+dx[di]
            y,x = ny,nx
            i+=1
        return ans