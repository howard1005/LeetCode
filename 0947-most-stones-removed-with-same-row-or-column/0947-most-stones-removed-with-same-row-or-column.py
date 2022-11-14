from collections import defaultdict,deque

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        ans = 0
        
        rd = defaultdict(list)
        cd = defaultdict(list)
        for x,y in stones:
            cd[x].append((x,y))
            rd[y].append((x,y))
        
        def bfs(sx,sy):
            ret = 0
            vis[(sx,sy)] = 1
            ret += 1
            dq = deque([(sx,sy)])
            while dq:
                x,y = dq.popleft()
                for nx,ny in cd[x]:
                    if (nx,ny) not in vis:
                        vis[(nx,ny)] = 1
                        ret += 1
                        dq.append((nx,ny))
                for nx,ny in rd[y]:
                    if (nx,ny) not in vis:
                        vis[(nx,ny)] = 1
                        ret += 1
                        dq.append((nx,ny))
            return ret
        
        vis = {}
        for x,y in stones:
            if (x,y) not in vis:
                ans += bfs(x,y) - 1
                
        return ans