class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        
        dp = [-1 for _ in range(1<<len(requests))]
        
        d = defaultdict(list)
        for i,(a,b) in enumerate(requests):
            d[a].append((b,i))
        
        def dfs(i,l,vis,res):
            nonlocal ans
            if len(l) >= 2 and l[0][0] == l[-1][0]:
                res.append([ri for _,ri in l[1:]])
                return
                
            for j,ri in d[i]:
                if vis[ri]:
                    continue
                vis[ri] = 1
                dfs(j,l+[(j,ri)],vis,res)
                vis[ri] = 0
        
        def findCycles(mask):
            vis = defaultdict(int)
            for i in range(len(requests)):
                if (mask>>i)&1 == 0:
                    vis[i] = 1
            
            cycles = []
            for i in range(n):
                dfs(i,[(i,-1)],vis,cycles)
            
            return cycles
        
        def proc(mask):
            if dp[mask] != -1:
                return dp[mask]
            dp[mask] = 0
            
            for cycle in findCycles(mask):
                nmask = mask
                for ri in cycle:
                    nmask ^= (1<<ri)
                dp[mask] = max(dp[mask],proc(nmask)+len(cycle))
                
            return dp[mask]

        return proc((1<<len(requests))-1)