class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ans = 0

        dp = {}

        m,n = len(grid),len(grid[0])

        def dfs(i,j):
            if j == n:
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = 0

            if i-1 >= 0 and j+1 < n and grid[i][j] < grid[i-1][j+1]:
                dp[(i,j)] = max(dp[(i,j)],dfs(i-1,j+1)+1)
            if i >= 0 and j+1 < n and grid[i][j] < grid[i][j+1]:
                dp[(i,j)] = max(dp[(i,j)],dfs(i,j+1)+1)
            if i+1 < m and j+1 < n and grid[i][j] < grid[i+1][j+1]:
                dp[(i,j)] = max(dp[(i,j)],dfs(i+1,j+1)+1)

            return dp[(i,j)]

        for i in range(m):
            ans = max(ans,dfs(i,0))

        return ans