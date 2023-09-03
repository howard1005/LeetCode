class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        bd = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            bd[i][0] = 1
        for j in range(n):
            bd[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                bd[i][j] += bd[i-1][j]+bd[i][j-1]
        return bd[-1][-1]