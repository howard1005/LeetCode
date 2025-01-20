class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        m,n = len(mat),len(mat[0])

        d = {}

        cntd = defaultdict(int)

        for i in range(m):
            for j in range(n):
                d[mat[i][j]] = (i,j)
        
        for idx,a in enumerate(arr):
            i,j = d[a]
            cntd[('r',i)] += 1
            if cntd[('r',i)] == n:
                return idx
            cntd[('c',j)] += 1
            if cntd[('c',j)] == m:
                return idx
        
        return -1

        

