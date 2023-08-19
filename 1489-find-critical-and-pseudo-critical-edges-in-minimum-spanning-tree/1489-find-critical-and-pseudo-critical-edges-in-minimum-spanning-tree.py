class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        l = [(i,a,b,c) for i,(a,b,c) in  enumerate(edges)]
        l.sort(key=lambda x: x[3])
        
        pars = None
        
        def clear():
            nonlocal pars
            pars = [_ for _ in range(n)]           
        
        def findPar(i):
            tl = []
            while pars[i] != i:
                tl.append(i)
                i = pars[i]
            for j in tl:
                pars[j] = i
            return i
        
        def union(i,j):
            pi,pj = findPar(i),findPar(j)
            pars[pj] = pi
            
        def isUnion(i,j):
            return findPar(i) == findPar(j)
        
        
        def mst(skip,choice):
            clear()
            cost = 0
            if choice != -1:
                a,b,c = edges[choice]
                union(a,b)
                cost += c
            for i,a,b,c in l:
                if choice == i or skip == i or isUnion(a,b):
                    continue
                union(a,b)
                cost += c
            return cost
        
        mn = mst(-1,-1)
        pool = set()
        option = set()
        for i,_,_,_ in l:
            if mst(-1,i) == mn:
                pool.add(i)
            if mst(i,-1) == mn:
                option.add(i)
        
        return [pool-option,pool&option]
        