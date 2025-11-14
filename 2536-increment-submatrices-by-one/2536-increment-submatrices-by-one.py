class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0 for _ in range(n)] for _ in range(n)]

        for a,b,c,d in queries:
            mat[a][b] += 1
            if c+1 < n:
                mat[c+1][b] -= 1
            if d+1 < n:
                mat[a][d+1] -= 1
            if c+1 < n and d+1 < n:
                mat[c+1][d+1] += 1
        

        for j in range(n):
            for i in range(1,n):
                mat[i][j] += mat[i-1][j]

        for i in range(n):
            for j in range(1,n):
                mat[i][j] += mat[i][j-1]

        return mat

        