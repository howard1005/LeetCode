class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        hvis,wvis = [[0 for _ in range(10)] for _ in range(9)],[[0 for _ in range(10)] for _ in range(9)]
        bvis = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    n = int(board[i][j])
                    if hvis[i][n] or wvis[j][n] or bvis[i//3][j//3][n]:
                        return False
                    hvis[i][n] += 1
                    wvis[j][n] += 1
                    bvis[i//3][j//3][n] += 1
        def dfs(i,j):
            if j == 9:
                i += 1
                j = 0
            if i == 9:
                return 0

            ret = 1
            if board[i][j] == '.':
                hs = set([n+1 for n,cnt in enumerate(hvis[i][1:]) if cnt == 0])
                ws = set([n+1 for n,cnt in enumerate(wvis[j][1:]) if cnt == 0])
                bs = set([n+1 for n,cnt in enumerate(bvis[i//3][j//3][1:]) if cnt == 0])
                s = hs & ws & bs
                while ret and s:
                    n = s.pop()
                    hvis[i][n] += 1
                    wvis[j][n] += 1
                    bvis[i//3][j//3][n] += 1
                    board[i][j] = str(n)
                    ret = dfs(i,j+1)
                    if ret == 0:
                        break
                    hvis[i][n] -= 1
                    wvis[j][n] -= 1
                    bvis[i//3][j//3][n] -= 1
                    board[i][j] = '.'
            else:
                ret = dfs(i,j+1)
            return ret
            
        dfs(0,0)

                    
        
        