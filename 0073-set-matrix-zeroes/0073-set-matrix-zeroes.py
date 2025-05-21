class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rd,cd = {},{}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rd[i] = 1
                    cd[j] = 1
        for r in rd:
            for j in range(len(matrix[0])):
                matrix[r][j] = 0
        for c in cd:
            for i in range(len(matrix)):
                matrix[i][c] = 0
        