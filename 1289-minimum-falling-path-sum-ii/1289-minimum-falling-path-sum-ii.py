from heapq import heappush,heappop

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        hq = []
        
        for j in range(n):
            dp[-1][j] = grid[-1][j]
            heappush(hq,(dp[-1][j],j)) 
        
        def getNotCol(j):
            if hq[0][1] != j:
                return hq[0][0]
            t = heappop(hq)
            ret = hq[0][0]
            heappush(hq,t)
            return ret
        
        
        for i in range(n-2,-1,-1):
            for j in range(n):
                dp[i][j] = grid[i][j] + getNotCol(j)
                
            hq = []
            for j in range(n):
                heappush(hq,(dp[i][j],j))
                
        return min(dp[0])
            