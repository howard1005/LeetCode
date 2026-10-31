class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        ans = 0

        MOD = 10**9+7

        dy,dx = [-1,0,1,0],[0,1,0,-1]

        m,n = len(grid),len(grid[0])

        dp = defaultdict(int)

        def dfs(i,j,di):
            if i == m-1 and j == n-1:
                return 1
            if i<0 or j<0 or i>=m or j>=n:
                return 0
            if (i,j,di) in dp:
                return dp[(i,j,di)]
            ret = 0
            if grid[i][j]:
                ndi = di^3
                ni,nj = i+dy[ndi],j+dx[ndi]
                ret = dfs(ni,nj,ndi)
                dp[(i,j,di)] = ret
                return ret
            for ndi in range(1,3):
                ni,nj = i+dy[ndi],j+dx[ndi]
                ret += dfs(ni,nj,ndi)
                ret %= MOD
            # print(i,j,di,ret)
            dp[(i,j,di)] = ret
            return ret

        ans = dfs(0,0,1)

        return ans