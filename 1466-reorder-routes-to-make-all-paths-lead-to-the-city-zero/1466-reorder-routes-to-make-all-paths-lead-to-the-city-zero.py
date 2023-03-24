class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ans = 0
        
        d = defaultdict(list)
        
        for a,b in connections:
            d[a].append((b,1))
            d[b].append((a,0))
        
        vis = {0:1}
        dq = deque([0])
        while dq:
            cur = dq.popleft()
            for ncur,ori in d[cur]:
                if ncur not in vis:
                    ans += ori
                    vis[ncur] = 1
                    dq.append(ncur)
        
        return ans