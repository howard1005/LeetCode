from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r,c = len(matrix),len(matrix[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        
        dp[0][0] = matrix[0][0]
        for i in range(1,r):
            dp[i][0] = dp[i-1][0] + matrix[i][0]
        for j in range(1,c):
            dp[0][j] = dp[0][j-1] + matrix[0][j]
        for i in range(1,r):
            for j in range(1,c):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i][j]
        
        def getDp(x,y):
            if x < 0 or y < 0:
                return 0
            return dp[y][x]
        
        def getCum(x1,y1,x2,y2):
            return getDp(x2,y2) - getDp(x2,y1-1) - getDp(x1-1,y2) + getDp(x1-1,y1-1)
        
        ans = 0
        def solve(r1,r2):
            nonlocal ans
            d = defaultdict(int)
            for j in range(c):
                cum = getCum(0,r1,j,r2)
                if cum == target:
                    ans += 1
                ans += d[cum-target]
                d[cum] += 1
                
        for r1 in range(r):
            for r2 in range(r1,r):
                solve(r1,r2)
            
        return ans