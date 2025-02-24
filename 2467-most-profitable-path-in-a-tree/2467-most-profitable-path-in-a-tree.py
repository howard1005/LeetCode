class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        ed = defaultdict(set)

        for a,b in edges:
            ed[a].add(b)
            ed[b].add(a)

        # print(ed)

        nd = defaultdict(list)
        
        def dfs(n):
            l = nd[n]
            # print(n,l)
            for nn in ed[n]:
                if nn != l[0]:
                    l.append(nn)
            for nn in l[1:]:
                nd[nn].append(n)
                dfs(nn)
        
        nd[0].append(-1)
        dfs(0)

        # print(nd)

        tbd = {}
        time = 0
        while bob != -1:
            tbd[bob] = time
            time += 1
            bob = nd[bob][0]

        # print(tbd)

        def dfs2(n,time):
            m = amount[n]
            if n in tbd:
                if tbd[n] < time:
                    m = 0
                elif tbd[n] == time:
                    m = amount[n]//2
            if len(nd[n]) == 1:
                return m
            ret = -inf
            # print(n,time,m)
            for nn in nd[n][1:]:
                ret = max(ret,dfs2(nn,time+1)+m)
            return ret
        
        ans = dfs2(0,0)

        return ans

        