class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = [True for _ in range(len(queries))]
        
        pars = [i for i in range(n)]
        
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
        
        edgeList.sort(key=lambda x: x[2])
        ql = [(idx,p,q,limit) for idx,(p,q,limit) in enumerate(queries)]
        ql.sort(key=lambda x: x[3])
        
        i = 0
        for idx,p,q,limit in ql:
            while i < len(edgeList) and limit > edgeList[i][2]:
                u,v,dis = edgeList[i]
                union(u,v)
                i += 1
            ans[idx] = isGroup(p,q)
                
        return ans