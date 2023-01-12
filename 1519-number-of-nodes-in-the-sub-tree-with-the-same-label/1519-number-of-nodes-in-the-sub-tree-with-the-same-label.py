from collections import defaultdict

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [None for _ in range(n)]
        
        d = defaultdict(list)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
            
        vis = {}
        def dfs(node):
            vd = defaultdict(int)
            for nn in d[node]:
                if nn in vis:
                    continue
                vis[nn] = 1
                _vd = dfs(nn)
                for k,v in _vd.items():
                    vd[k] += v
            label = labels[node]
            vd[label] += 1
            ans[node] = vd[label]
            return vd
        vis[0] = 1
        dfs(0)
        
        return ans