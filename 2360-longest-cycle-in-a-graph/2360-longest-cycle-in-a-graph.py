class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        ans = -1
        
        STEP = 0
        
        vis = {}
        def bfs(s):
            nonlocal ans
            vis[s] = STEP
            dq = deque([s])
            while dq:
                cur = dq.popleft()
                ncur = edges[cur]
                if ncur == -1:
                    continue
                if ncur in vis:
                    if vis[ncur] >= STEP:
                        ans = max(ans,vis[cur] - vis[ncur] + 1)
                else:
                    vis[ncur] = vis[cur] + 1
                    dq.append(ncur)
        
        for i in range(len(edges)):
            if i not in vis:
                bfs(i)
                STEP += 1000000
        
        
        return ans