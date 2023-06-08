class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        
        n,m = len(grid),len(grid[0])
        i,j = 0,m-1
        while i < n:
            if grid[i][j] >= 0:
                i += 1
                continue
            if j == 0 or grid[i][j-1] >= 0:
                ans += m-j
                i += 1
                continue
            j -= 1
        
        return ans