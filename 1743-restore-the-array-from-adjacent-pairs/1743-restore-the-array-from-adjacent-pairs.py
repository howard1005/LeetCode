class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        ans = []
        
        d = defaultdict(list)
        
        for a,b in adjacentPairs:
            d[a].append(b)
            d[b].append(a)
        
        dq = deque()
        vis = {}
        for k,v in d.items():
            if len(v) == 1:
                vis[k] = 1
                dq.append(k)
                break
                
        while dq:
            cur = dq.popleft()
            ans.append(cur)
            for ncur in d[cur]:
                if ncur not in vis:
                    vis[ncur] = 1
                    dq.append(ncur)
        
        return ans