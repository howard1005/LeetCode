class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r,c = len(grid),len(grid[0])
        ans = [[0 for _ in range(c)] for _ in range(r)]
        k = (r*c-k)%(r*c)
        for i in range(r):
            for j in range(c):
                ii,jj = k//c,k%c
                ans[i][j] = grid[ii][jj]
                k = (k+1)%(r*c)
        return ans