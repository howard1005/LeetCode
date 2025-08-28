class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)

        m,n = len(grid),len(grid[0])

        for i in range(m):
            for j in range(n):
                d[i-j].append(grid[i][j])
        
        for k,l in d.items():
            if k>=0:
                l.sort()
            else:
                l.sort(reverse=True)

        for i in range(m):
            for j in range(n):
                grid[i][j] = d[i-j].pop()

        return grid