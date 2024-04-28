class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        v = [[] for _ in range(n)]
        for edge in edges:
            v[edge[0]].append(edge[1])
            v[edge[1]].append(edge[0])
        
        l = [[] for _ in range(n)]
        vis = [0 for _ in range(n)]
        def dfs(i):
            vis[i] = 1
            ret = [0,1]
            for nv in v[i]:
                if vis[nv]:
                    continue
                t = dfs(nv)
                ret[0] += t[0]+t[1]
                ret[1] += t[1]
            l[i] = ret[:]
            return ret
        dfs(0)
        
        ans = [0 for _ in range(n)]
        vis = [0 for _ in range(n)]
        def dfs2(i,pi):
            vis[i] = 1
            if pi == -1:
                ans[i] = l[i][0]
            else:
                ans[i] = ans[pi]-2*l[i][1]+n
            for nv in v[i]:
                if vis[nv]:
                    continue
                dfs2(nv,i)
        dfs2(0,-1)
        
        return ans
        
        
        
        