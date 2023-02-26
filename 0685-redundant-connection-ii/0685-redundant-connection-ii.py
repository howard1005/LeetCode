class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        ind = defaultdict(list)
        outd = defaultdict(int)
        d = defaultdict(int)
        isP = None
        
        def canDel(u,v):
            return outd[u] + len(ind[u]) >= 2 and outd[v] + len(ind[v]) >= 2
        
        for u,v in edges:
            ind[v].append(u)
            outd[u] += 1
            if (v,u) in d:
                isP = (v,u)
            d[(u,v)] = 1
            
        for v,us in ind.items():
            if len(us) == 2:
                us.reverse()
                if isP:
                    for u in us:
                        if (u,v) == isP or (u,v) == isP[::-1]:
                            return [u,v]
                for u in us:
                    if canDel(u,v):
                        return [u,v]
                    
        for u,v in edges[::-1]:
            us = ind[v]
            if len(us) == 1:
                if isP:
                    for u in us:
                        if (u,v) == isP or (u,v) == isP[::-1]:
                            return [u,v]
                else:
                    for u in us:
                        if canDel(u,v):
                            return [u,v]
        return []