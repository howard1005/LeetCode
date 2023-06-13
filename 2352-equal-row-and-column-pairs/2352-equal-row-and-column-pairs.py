class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        
        n = len(grid)
        d = defaultdict(int)
        for r in grid:
            d[tuple(r)] += 1
        for j in range(n):
            t = tuple(grid[i][j] for i in range(n))
            if t in d:
                ans += d[t]
        
        return ans