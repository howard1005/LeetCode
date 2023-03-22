class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(list)
        
        for a,b,dist in roads:
            d[a].append((b,dist))
            d[b].append((a,dist))
        
        mn = inf
        vis = {1:1}
        dq = deque([1])
        while dq:
            cur = dq.popleft()
            for ncur,dist in d[cur]:
                mn = min(mn,dist)
                if ncur not in vis:
                    vis[ncur] = 1
                    dq.append(ncur)
                    
        return mn
            
                
                