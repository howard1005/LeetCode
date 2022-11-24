class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        m,n = len(board),len(board[0])
        vis = [[0 for _ in range(n)] for _ in range(m)]
        def dfs(y,x,i):
            if i == len(word):
                return True
            for di in range(4):
                ny,nx = y+dy[di],x+dx[di]
                if ny<0 or nx<0 or ny>=m or nx>=n or vis[ny][nx] or board[ny][nx] != word[i]:
                    continue
                vis[ny][nx] = 1
                if dfs(ny,nx,i+1):
                    return True
                vis[ny][nx] = 0
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    vis[i][j] = 1
                    if dfs(i,j,1):
                        return True
                    vis[i][j] = 0
        return False