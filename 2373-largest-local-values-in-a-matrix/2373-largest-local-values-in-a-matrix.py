class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        ans = [[0 for _ in range(n-2)] for _ in range(n-2)] 

        for i in range(n):
            for j in range(n):
                if i >= n-2 or j >= n-2:
                    continue
                mx = 0
                for ii in range(3):
                    for jj in range(3):
                        mx = max(mx,grid[i+ii][j+jj])
                ans[i][j] = mx

        return ans