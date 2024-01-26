class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dy = [-1,0,1,0]
        dx = [0,1,0,-1]
        dp = [[[-1 for _ in range(maxMove+1)] for _ in range(n)] for _ in range(m)]
        
        def dfs(y,x,mm):
            if mm <= 0:
                return 0
            cnt = dp[y][x][mm]
            if cnt != -1:
                return cnt
            else:
                dp[y][x][mm] = 0
            cnt = 0
            for di in range(4):
                ny = y + dy[di]
                nx = x + dx[di]
                if ny<0 or nx<0 or ny>=m or nx>=n:
                    cnt = (cnt + 1) % 1000000007
                else:
                    cnt = (cnt + dfs(ny,nx,mm-1)) % 1000000007
            dp[y][x][mm] = cnt
            return cnt
        
        return dfs(startRow, startColumn, maxMove)