class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m,n = len(grid),len(grid[0])

        l = []
        for i in range(m):
            cum = 0
            for j in range(n):
                cum += grid[i][j]
            l.append(cum)
        tot = sum(l)
        if tot%2 == 0:
            target = tot//2
            p = 0
            for i in range(len(l)):
                p += l[i]
                if p == target:
                    return True

        l = []
        for j in range(n):
            cum = 0
            for i in range(m):
                cum += grid[i][j]
            l.append(cum)
        tot = sum(l)
        if tot%2 == 0:
            target = tot//2
            p = 0
            for i in range(len(l)):
                p += l[i]
                if p == target:
                    return True
        
        return False
        