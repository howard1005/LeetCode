class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        ans = 0

        ed = defaultdict(set)

        for a,b in hierarchy:
            ed[a].add(b)

        @cache
        def td_proc(i,par):
            td = defaultdict(lambda:inf)
            for j in ed[i]:
                cd = {} # profit : cost
                for nbg in range(budget+1):
                    p = dfs(j,par,nbg)
                    if p not in cd:
                        cd[p] = nbg

                for p1 in sorted(td.keys(),reverse=True):
                    for p2,c2 in cd.items():
                        if td[p1]+c2 <= budget:
                            td[p1+p2] = min(td[p1+p2],td[p1]+c2)
                
                for p,c in cd.items():
                    td[p] = min(td[p],c)

                rtd = defaultdict(lambda:-inf)
                for p1,c1 in td.items():
                    rtd[c1] = max(rtd[c1],p1)
                ttd = defaultdict(lambda:inf)
                for c1,p1 in rtd.items():
                    ttd[p1] = c1
                td = ttd
            return td

        @cache
        def proc(i,par,bg):
            td = td_proc(i,par)

            cands = []
            for p,c in td.items():
                if c <= bg:
                    cands.append((p,c))
            cands.sort(key=lambda x:(-x[0],x[1]))

            # if len(cands)>=200:
            #     print(len(cands))
            # print(i,par,bg,td,cands)

            for p,c in cands:
                if c <= bg:
                    return p
            
            return 0
            
        @cache
        def dfs(i,par,bg):
            ret = 0

            profit1 = proc(i,0,bg)
                
            need = present[i-1]//2 if par else present[i-1]
            profit2 = (proc(i,1,bg-need) + future[i-1]-need) if bg>=need else 0

            # print(f"i {i} profit1 {profit1} profit2 {profit2} need {need} {future[i-1]-need}")
            
            ret = max(profit1,profit2)

            return ret

        ans = dfs(1,0,budget)

        return ans