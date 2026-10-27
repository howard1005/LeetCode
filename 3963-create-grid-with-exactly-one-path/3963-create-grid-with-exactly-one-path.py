class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#' for _ in range(n)] for _ in range(m)]

        for j in range(n):
            grid[0][j] = '.'
        for i in range(m):
            grid[i][-1] = '.'

        ans = []

        for r in grid:
            # print(r)
            ans.append(''.join(r))
        
        return ans