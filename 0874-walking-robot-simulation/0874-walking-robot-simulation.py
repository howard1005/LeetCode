class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = 0

        dy,dx = [-1,0,1,0],[0,1,0,-1]

        od = set()
        for x,y in obstacles:
            od.add((-y,x))
            
        di = 0
        y,x = 0,0
        for cmd in commands:
            if cmd == -2:
                di = (di-1+4)%4
            elif cmd == -1:
                di = (di+1)%4
            else:
                cnt = cmd
                while cnt:
                    ny = y + dy[di]
                    nx = x + dx[di]
                    if (ny,nx) not in od:
                        y,x = ny,nx
                    cnt -= 1
            ans = max(ans,y*y+x*x)

        return ans