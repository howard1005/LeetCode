class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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
        return True
        