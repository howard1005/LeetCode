class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m,n = len(mat),len(mat[0])

        tmat = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i&1:
                    tmat[i][(j+k)%n] = mat[i][j]
                else:
                    tmat[i][(j-k+n*1000)%n] = mat[i][j]

        for i in range(m):
            for j in range(n):
                if tmat[i][j] != mat[i][j]:
                    return False

        return True