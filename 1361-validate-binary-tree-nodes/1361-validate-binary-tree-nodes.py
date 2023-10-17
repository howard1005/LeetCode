class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        pars = [i for i in range(n)]
        
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
            if pi != pj:
                pars[pi] = pj
        
        def isUnion(i,j):
            return findPar(i) == findPar(j)
        
        d = defaultdict(int)
        
        for i in range(n):
            lc,rc = leftChild[i],rightChild[i]
            if lc != -1:
                if d[lc] >= 1:
                    return False
                d[lc] += 1
                if isUnion(i,lc):
                    return False
                union(i,lc)
            if rc != -1:
                if d[rc] >= 1:
                    return False
                d[rc] += 1
                if isUnion(i,rc):
                    return False
                union(i,rc)
        
        for i in range(n-1):
            if findPar(i) != findPar(i+1):
                return False
            
        return True