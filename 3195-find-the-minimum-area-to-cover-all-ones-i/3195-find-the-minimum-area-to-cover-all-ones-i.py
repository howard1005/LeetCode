class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        mny,mnx,mxy,mxx = inf,inf,-1,-1

        m,n = len(grid),len(grid[0])
        for y in range(m):
            for x in range(n):
                if grid[y][x]:
                    mny = min(mny,y)
                    mxy = max(mxy,y)
                    mnx = min(mnx,x)
                    mxx = max(mxx,x)

        ans = (mxy-mny+1)*(mxx-mnx+1)

        return ans