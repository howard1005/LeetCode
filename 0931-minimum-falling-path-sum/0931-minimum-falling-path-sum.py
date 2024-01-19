class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[inf for _ in range(n)] for _ in range(n)]
        for j in range(n):
            dp[-1][j] = matrix[-1][j]
        for i in range(n-2,-1,-1):
            for j in range(n):
                for k in range(-1,2):
                    if 0<= j+k and j+k < n: 
                        dp[i][j] = min(dp[i][j],dp[i+1][j+k]+matrix[i][j])
        return min(dp[0])