class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        
        vis = set()

        dy,dx = [-1,0,1,0],[0,1,0,-1]

        cnt = rows*cols
        di = 1
        y,x = rStart,cStart
        vis.add((y,x))
        ans.append((y,x))
        cnt -= 1
        while cnt:
            ny,nx = y+dy[di],x+dx[di]
            vis.add((ny,nx))
            if 0<=ny and ny<rows and 0<=nx and nx<cols:
                ans.append((ny,nx))
                cnt -= 1
            y,x = ny,nx
            if (y+dy[(di+1)%4],x+dx[(di+1)%4]) not in vis:
                di = (di+1)%4

        return ans
            
            