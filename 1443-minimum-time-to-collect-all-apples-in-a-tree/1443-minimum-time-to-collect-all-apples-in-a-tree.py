from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        ans = 0
        
        d = defaultdict(list)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
            
        vis = {}
        def dfs(n):
            nonlocal ans
            ret = hasApple[n]
            for nn in d[n]:
                if nn in vis:
                    continue
                vis[nn] = 1
                if dfs(nn):
                    ret = True
                    ans += 2
            return ret
        vis[0] = 1
        dfs(0)
        
        return ans