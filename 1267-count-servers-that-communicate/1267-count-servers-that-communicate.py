class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ans = 0
        
        m,n = len(grid),len(grid[0])
        
        rd,cd = defaultdict(int),defaultdict(int)

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rd[i] += 1
                    cd[j] += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if rd[i] > 1 or cd[j] > 1:
                        ans += 1

        return ans