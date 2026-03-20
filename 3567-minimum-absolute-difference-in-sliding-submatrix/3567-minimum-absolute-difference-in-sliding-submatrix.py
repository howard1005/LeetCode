class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])

        ans = [[0 for _ in range(n - k + 1)] for _ in range(m - k + 1)]

        for i in range(m-k+1):
            for j in range(n-k+1):
                l = []
                for a in range(i,i+k):
                    for b in range(j,j+k):
                        l.append(grid[a][b])
                mn = inf
                l = list(set(l))
                l.sort()
                # print(l)
                if len(l) == 1:
                    mn = 0
                for a in range(len(l)-1):
                    mn = min(mn,l[a+1]-l[a])
                ans[i][j] = mn

        return ans
                        