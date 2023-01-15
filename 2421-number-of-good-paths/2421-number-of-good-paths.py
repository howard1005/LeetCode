from collections import deque
from sortedcontainers import SortedList

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        ans = 0
        
        d = defaultdict(list)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
            
        par = [i for i in range(len(vals))]
        
        def getPar(i):
            tl = []
            while i != par[i]:
                tl.append(i)
                i = par[i]
            for j in tl:
                par[j] = i
            return i
        
        def merge(i,j):
            i,j = getPar(i),getPar(j)
            par[i] = j
        
        dd = defaultdict(list)
        for i,v in enumerate(vals):
            dd[v].append(i)
            
        for k in sorted(dd.keys()):
            for n in dd[k]:
                for nn in d[n]:
                    if vals[nn] <= k:
                        merge(n,nn)
            ddd = defaultdict(int)
            for n in dd[k]:
                ddd[getPar(n)] += 1
            for cnt in ddd.values():
                ans += cnt*(cnt+1)//2
        
        return ans