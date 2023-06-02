class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        ans = 0
        
        def bfs(i):
            ret = 1
            vis = {i:1}
            dq = deque([i])
            while dq:
                x,y,r = bombs[dq.popleft()]
                for j in range(len(bombs)):
                    if j not in vis:
                        xx,yy,rr = bombs[j]
                        if (xx-x)**2+(yy-y)**2 <= r**2:
                            ret += 1
                            vis[j] = 1
                            dq.append(j)
            return ret
                        
        for i in range(len(bombs)):
            ans = max(ans,bfs(i))
                
        return ans