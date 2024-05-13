class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ans = 0
        
        m,n = len(grid),len(grid[0])

        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1
        
        for j in range(1,n):
            cnt = 0
            for i in range(m):
                cnt += grid[i][j]
            if cnt <= m//2:
                for i in range(m):
                    grid[i][j] ^= 1
        
        for i in range(m):
            b = 0
            for j in range(n):
                b = (b<<1)+grid[i][j]
            ans += b

        return ans