class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        ans = []

        n = len(edges1)+1
        m = len(edges2)+1
        
        ed1 = defaultdict(set)
        for a,b in edges1:
            ed1[a].add(b)
            ed1[b].add(a)

        ed2 = defaultdict(set)
        for a,b in edges2:
            ed2[a].add(b)
            ed2[b].add(a)

        d1 = defaultdict(lambda:1)
        d2 = defaultdict(lambda:1)
        

        def dfs(par,node,dep,ed,kk,d):
            ret = [(node,dep)]
            l = []
            for nn in ed[node]:
                if nn == par:
                    continue
                tl = dfs(node,nn,dep+1,ed,kk,d)
                l.append(tl)
                ret.extend(tl)

            # print(node,l)

            for i in range(len(l)):
                for a,c1 in l[i]:
                    if c1-dep <= kk:
                        d[node] += 1
                        d[a] += 1

            for i in range(len(l)):
                for j in range(i+1,len(l)):
                    for a,c1 in l[i]:
                        for b,c2 in l[j]:
                            if c1-dep+c2-dep <= kk:
                                d[a] += 1
                                d[b] += 1

            

            return ret
            
            
        dfs(-1,0,0,ed1,k,d1)
        dfs(-1,0,0,ed2,k-1,d2)

        # print(d1)
        # print(d2)

        mx = 0
        if k:
            for i in range(m):
                mx = max(mx,d2[i])
        # print(mx)

        for i in range(n):
            ans.append(d1[i]+mx)

        return ans