class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    for di in range(4):
                        ny,nx = dy[di]+i,dx[di]+j
                        if ny<0 or nx<0 or ny>=n or nx>=m or grid[ny][nx] == 0:
                            ans += 1
        return ans
                        
                    