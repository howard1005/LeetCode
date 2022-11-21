from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ans = inf
        
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        vis = {}
        dq = deque([tuple(entrance)+(0,)])
        r,c = len(maze),len(maze[0])
        
        while dq:
            y,x,d = dq.popleft()
            if (y,x) != tuple(entrance) and (y in (0,r-1) or x in (0,c-1)):
                ans = min(ans,d)
            for di in range(4):
                ny,nx = y+dy[di],x+dx[di]
                if ny<0 or nx<0 or ny>=r or nx>=c or (ny,nx) in vis or maze[ny][nx]=='+':
                    continue
                vis[(ny,nx)] = 1
                dq.append((ny,nx,d+1))
                
        if ans == inf: return -1
        return ans