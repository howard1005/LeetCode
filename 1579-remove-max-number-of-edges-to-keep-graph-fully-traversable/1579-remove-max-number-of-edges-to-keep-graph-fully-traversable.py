class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:                 
        edges.sort(reverse=True)
        
        cnts = [2 if t == 3 else 1 for t,_,_ in edges]
    
        
        def proc(ft):
            pars = [i for i in range(n+1)]
        
            def findPar(i):
                tl = []
                while i != pars[i]:
                    tl.append(i)
                    i = pars[i]
                for ii in tl:
                    pars[ii] = i
                return i

            def union(i,j):
                ii,jj = findPar(i),findPar(j)
                pars[jj] = ii

            def isGroup(i,j):
                return findPar(i) == findPar(j)
            
            for i,(t,u,v) in enumerate(edges):
                if t == ft:
                    continue
                if isGroup(u,v):
                    cnts[i] -= 1
                else:
                    union(u,v)
            
            vis = {}
            for i in pars[1:]:
                vis[findPar(i)] = 1
            return len(vis) != 1
        
        if proc(2) or proc(1):
            return -1
        
        return cnts.count(0)