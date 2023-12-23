class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        d = {
            'N':0,
            'E':1,
            'S':2,
            'W':3
        }
        
        vis = {(0,0):1}
        y,x = 0,0
        for c in path:
            di = d[c]
            ny,nx = y+dy[di],x+dx[di]
            if (ny,nx) in vis:
                return True
            vis[(ny,nx)] = 1
            y,x = ny,nx
        
        return False