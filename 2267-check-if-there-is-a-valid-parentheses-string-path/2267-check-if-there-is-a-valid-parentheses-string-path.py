class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m,n = len(grid),len(grid[0])

        @cache
        def dfs(i,j,k):
            if m-i+n-j-1 < k:
                return False

            p = 1 if grid[i][j] == '(' else -1

            if i == m-1 and j == n-1:
                if k == 1 and p == -1:
                    return True 
                return False

            ret = False
            nk = k+p
            if i+1 < m and nk >= 0:
                ret |= dfs(i+1,j,nk)
            if not ret and j+1 < n and nk >= 0:
                ret |= dfs(i,j+1,nk)

            # print(i,j,k)
            return ret

        return dfs(0,0,0)
