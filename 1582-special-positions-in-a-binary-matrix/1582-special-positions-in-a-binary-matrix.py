class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        m,n = len(mat),len(mat[0])
        
        d = defaultdict(int)
        
        for i in range(m):
            t = []
            for j in range(n):
                if mat[i][j]:
                    t.append((i,j))
            if len(t) == 1:
                d[t[0]] += 1
                
        for j in range(n):
            t = []
            for i in range(m):
                if mat[i][j]:
                    t.append((i,j))
            if len(t) == 1:
                d[t[0]] += 1
        
        ans = 0
        for k,v in d.items():
            if v == 2:
                ans += 1
                
        return ans
                