class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        ans = 0
        
        d = defaultdict(list)
        for a,b in roads:
            d[a].append(b)
            d[b].append(a)
        
        vis = {}
        def dfs(n):
            nonlocal ans
            ret = 1
            for nn in d[n]:
                if nn not in vis:
                    vis[nn] = 1
                    ret += dfs(nn)
            if n != 0:
                ans += ret//seats + (1 if ret%seats else 0)
            return ret
        vis[0] = 1
        dfs(0)
        
        return ans